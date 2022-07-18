<template>


    <div class="q-pa-md q-gutter-sm">
        <div id="divbtn">
            <q-page-sticky position="bottom-right" :offset="[18, 18]" v-if="loginStore.autor.estado==1">
                <q-btn fab icon="add" color="amber" class="inset-shadow-down" @click="layout = true">
                    <q-tooltip class="bg-amber text-black shadow-4" :offset="[10, 10]">
                        Agregar Noticia
                    </q-tooltip>
                </q-btn>
            </q-page-sticky>
        </div>


        <q-dialog v-model="layout">
            <q-layout view="hHh lpR fFf" class="bg-white ventana">
                <q-page-container>

                    <div class="q-pa-md" style="max-width: 100%">

                        <q-form class="q-gutter-md">

                            <q-input color="grey-3" label-color="dorado" outlined v-model="tituloTxt" label="Titulo de la noticia" 
                            :rules="[this.required,this.short, this.long]" />

                            <q-input v-model="textoTxt" filled type="textarea"
                                    :rules="[this.required,this.short]" 
                                    color="dorado" 
                                    label="Texto de la noticia"
                            />

                            <div class="divbtn"> 
                                <q-btn label="Postear" type="submit" color="dorado" @click="submit" />
                            </div>

                        </q-form>

                    </div>

                </q-page-container>
            </q-layout>
        </q-dialog>
    </div>
</template>

<script>
import { dateFormat } from "../assets/funciones";
import { ref } from 'vue'
import { useLoginStore } from 'src/stores/login'
import { useNoticiaStore } from 'src/stores/noticia';

export default {
    name: "ComentarioList",
    setup() {
        const loginStore = useLoginStore();
        const noticiaStore = useNoticiaStore();

        return {
            layout: ref(false),
            loginStore,
            noticiaStore,
        };
    },
    data() {
        return {
            textoTxt: "",
            tituloTxt: ""
        };
    },
    methods: {
        dateFormat,

        required (val) {
            return  (val && val.length > 0 || 'Este campo no puede quedar vacio')
        },

        short(val) {
            return  (val && val.length > 5 || 'Demasiado corto')
        },

        long(val) {
            return  (val && val.length < 200 || 'Demasiado largo. Por favor, menor a 200 caracteres')
        },

        submit () {
			this.noticiaStore.noticiaNueva (this.tituloTxt, this.textoTxt, this.loginStore.autor.id);
			if (this.noticiaStore.HTTPstatus == 400) {
                console.log(this.noticiaStore.HTTPstatus)
				this.$q.notify({type:'negative', message:'Ha fallado la creación de la noticia.'})
			} else {
                this.layout = false;
            }
        }
        
    },
    created() {
    },
};
</script>

<style scoped>

.ventana {
    min-height: 0 !important;
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