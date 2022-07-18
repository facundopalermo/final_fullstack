<template>
    <div class="q-pa-md q-gutter-sm">
        <div class="divbtn">
            <q-btn flat style="color: #deb03f" label="Ver comentarios" @click="layout = true" />
        </div>


        <q-dialog v-model="layout">
            <q-layout view="hHh lpR fFf" class="bg-white ventana">
                <q-page-container>

                    <h2>Comentarios sobre <br/><span id="titulo">{{ titulo }}</span></h2>

                    <div v-if="!comentarios.length" id="comentario">
                        Esta noticia no tiene comentarios. Se el primero!.
                    </div>

                    <div id="comentario" v-for="comentario in comentarios" :key="comentario.code">

                        <avatar-comp :nombre="comentario.autor" :fecha="dateFormat(comentario.fecha)" />

                        <p>{{ comentario.texto }}</p>

                    </div>
                    <div class="divbtn">
                        <q-btn flat text-color="dorado" icon="insert_comment" label="Comentar"
                            @click="comentar = true" v-if="loginStore.autor.estado==1"/>
                    </div>

                </q-page-container>
            </q-layout>
        </q-dialog>

        <q-dialog v-model="comentar" transition-show="scale" transition-hide="scale">
            <q-card class="bg-dorado text-white" style="width: 500px">
                <q-card-section>
                    <div class="text-h6">Agregar comentario</div>
                </q-card-section>

                <q-card-section class="bg-white">
                    <q-input
                        label="Su comentario (Máximo 250 caracteres)"
                        v-model="texto"
                        color="dorado"
                        filled
                        autogrow
                        :rules="[this.required, this.short, this.long]"
                    />
                </q-card-section>

                <q-card-actions align="right" class="bg-white text-teal">
                    <q-btn flat label="Comentar" v-close-popup text-color="dorado" @click="submit"/>
                </q-card-actions>
            </q-card>
        </q-dialog>

    </div>
</template>

<script>
import axios from "axios";
import { dateFormat } from "../assets/funciones";
import { ref } from 'vue'
import AvatarComp from 'components/AvatarComp.vue';
import { useLoginStore } from 'src/stores/login'

export default {
    name: "ComentarioList",
    
    setup() {
        const loginStore = useLoginStore();

        return {
            layout: ref(false),
            comentar: ref(false),
            loginStore
        }
    },
    
    data() {
        return {
            comentarios: [],
            texto: ''
        };
    },
    props: {
        noticia: Number,
        titulo: String
    },
    methods: {
        dateFormat,
        async getComentarios(noticia) {
            let url = "http://localhost:8000/api/noticias/" + noticia + "/comentarios/";
            let data = await axios.get(url);
            this.comentarios = data.data;
        },
        required (val) {
            return  (val && val.length > 0 || 'Este campo no puede quedar vacio')
        },

        short(val) {
            return  (val && val.length > 2 || 'Demasiado corto')
        },

        long(val) {
            return  (val && val.length < 250 || 'Demasiado largo. Por favor, menor a 250 caracteres')
        },

        async submit () {
            console.log('click')
            const data = await axios.post('http://localhost:8000/api/comentarios/', {
				texto: this.texto,
				fecha: new Date().toISOString(),
                autor_id: this.loginStore.autor.id,
                noticia: this.noticia
			}, {
				withCredentials: false,
				headers: {
						'Content-Type': 'application/json',
                        'accept': 'application/json',
				}
			}).catch((error) => {
				if(error.response) {
					console.log(error.message)
					return error.response.status;
				}
			})

			if(data.status == 201) {
                this.comentar = false
                this.getComentarios(this.noticia)
			} else {
                this.$q.notify({type:'negative', message:'Ha fallado el comentar.'})
			}
        }
    },
    created() {
        this.getComentarios(this.noticia);
    },
    components: { AvatarComp }
};
</script>

<style scoped>

.ventana {
    min-height: 0 !important;
    border: solid #deb03f 5px;
}

h2 {
    line-height: 1.5;
    padding-inline: 10px;
    font-size:medium;
    font-weight: bold;
    color: darkslategray;
}

h3 {
    line-height: 0px;
    padding-inline: 10px;
    font-size:medium;
    color: darkslategray;
}

#comt_autor {
    color:#6200ffe7;
    font-weight: bolder;
}

p {
    font-size: large;
    padding-inline: 10px;
}

#comentario {
    margin: 5px;
    padding: 5px;
    border-radius: 10px;
    border-style: solid;
    background-color:#fffce0 ;
}

.divbtn {
    text-align:right;
}

#titulo {
    color:black;
    font-size: large;
}

#avatar {
    width: 48px !important;
    height: 48px !important;
}

</style>