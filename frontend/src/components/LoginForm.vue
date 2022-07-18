<template>
  <div class="column q-pa-lg">
    <div class="row">
        <q-card square class="shadow-24" style="width:400px;">

			<q-card-section class="bg-dorado">
				<h4 class="text-h5 text-white q-my-md">{{ title }}</h4>        
			</q-card-section>

            <q-card-section>
				<q-fab
					color="primary" @click="switchTypeForm"
					icon="add"
					class="absolute"
					style="top: 0; right: 12px; transform: translateY(-50%);"
				>
					<q-tooltip>Nuevo autor</q-tooltip>
				</q-fab>

				<q-form class="q-px-sm q-pt-xl">
					<q-input 
						ref="email"
						square 
						clearable 
						v-model="email" 
						type="email"
						lazy-rules
						:rules="[this.required,this.isEmail,this.short]"
						label="Email">
						<template v-slot:prepend>
							<q-icon name="email" />
						</template>
					</q-input>

					<q-input 
						ref="nombre"
						v-if="register" 
						square 
						clearable 
						v-model="first_name"
						lazy-rules
						:rules="[this.required]"
						label="Nombre">
						<template v-slot:prepend>
							<q-icon name="description"/>
						</template>
					</q-input>

					<q-input 
						ref="apellido"
						v-if="register" 
						square 
						clearable 
						v-model="last_name"
						lazy-rules
						:rules="[this.required]"
						label="Apellido">
						<template v-slot:prepend>
							<q-icon name="description"/>
						</template>
					</q-input>

					<q-input 
						ref="fechanac"
						v-if="register" 
						square 
						clearable 
						v-model="fecha_nac"
						lazy-rules
						:rules="[this.required]"
						type="date"
						label="Fecha de nacimiento">
						<template v-slot:prepend>
							<q-icon name="calendar_month"/>
						</template>
					</q-input>

					<q-input 
						ref="username"
						v-if="register" 
						square 
						clearable 
						v-model="username"
						lazy-rules
						:rules="[this.required,this.short]"
						type="username"
						label="Usuario">
						<template v-slot:prepend>
							<q-icon name="person"/>
						</template>
					</q-input>


					<q-input  
						ref="password"
						square 
						clearable 
						v-model="password"
						:type="passwordFieldType"  
						lazy-rules
						:rules="[this.required,this.short]"
						label="Contraseña">
						<template v-slot:prepend>
							<q-icon name="lock" />
						</template>
						<template v-slot:append>
							<q-icon 
								:name="visibilityIcon"
								@click="switchVisibility"
								class="cursor-pointer" />
						</template>
					</q-input>

					<q-input 
						ref="repassword"
						v-if="register" 
						square 
						clearable 
						v-model="repassword"
						:type="passwordFieldType" 
						lazy-rules
						:rules="[this.required,this.short,this.diffPassword]"
						label="Repetir contraseña">
						<template v-slot:prepend>
							<q-icon name="lock" />
						</template>
						<template v-slot:append>
							<q-icon 
							:name="visibilityIcon"
							@click="switchVisibility"
							class="cursor-pointer" />
						</template>
					</q-input>

                </q-form>
            </q-card-section>

			<q-card-actions class="q-px-lg">
				<q-btn 
					unelevated 
					size="lg" 
					color="dorado"
					@click="submit"
					class="full-width text-white"
					:label="btnLabel" />
			</q-card-actions>
          </q-card>
      </div>
  </div>
</template>

<script>

import { useLoginStore } from 'src/stores/login'


const loginStore = useLoginStore();

export default {
	name: 'LoginForm',
		
	data() {
        return {
            title: 'Iniciar sesión',
            email: '',
            username: '',
			first_name: '',
			last_name: '',
			fecha_nac: '',
            password: '',
            repassword: '',
            register: false,
            passwordFieldType: 'password',
            btnLabel: 'Entrar',
            visibility: false,
            visibilityIcon: 'visibility'
        }
    },
    methods: {

        required (val) {
            return  (val && val.length > 0 || 'Este campo no puede quedar vacio')
        },

        diffPassword (val) {
            const val2 = this.password
            console.log(val + ' ' + val2);
            return (val && (val===val2) || 'No coinciden las contraseñas')
        },

        short(val) {
            return  (val && val.length > 3 || 'Demasiado corta!')
        },

        isEmail (val) {
            const emailPattern = /^(?=[a-zA-Z0-9@._%+-]{6,254}$)[a-zA-Z0-9._%+-]{1,64}@(?:[a-zA-Z0-9-]{1,63}\.){1,8}[a-zA-Z]{2,63}$/
            return (emailPattern.test(val) || 'El formato del email es incorrecto')
        },

        async submit () {
            if (this.register){
				loginStore.registrar (this.first_name, this.last_name,	this.password, this.email, this.username, this.fecha_nac);
				if (loginStore.HTTPstatus == 400) {
					this.$q.notify({type:'negative', message:'Hay datos incorrectos! El usuario no se ha creado'})
				}
            } else {
				await loginStore.login(this.email, this.password)
				
				if (loginStore.HTTPstatus == 400) {
					this.$q.notify({type:'negative', message:'Datos incorrectos!'})
				} else if (loginStore.HTTPstatus == 202) {
					this.$router.push({ path: '/' })
				}
            }
        },

        switchTypeForm(){ 
            this.register = !this.register
            this.title = this.register ? 'Nuevo autor' : 'Iniciar sesión'
            this.btnLabel = this.register ? 'Registrarse' : 'Entrar'
        },

        switchVisibility() {
            this.visibility = !this.visibility
            this.passwordFieldType = this.visibility ? 'text' : 'password'
            this.visibilityIcon =  this.visibility ? 'visibility_off' : 'visibility'
        }
    }
}
</script>