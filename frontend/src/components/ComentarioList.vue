<template>
    <div class="q-pa-md q-gutter-sm">
        <div id="divbtn">
            <q-btn label="Ver comentarios" id="btncomentario" @click="layout = true" />
        </div>
        

        <q-dialog v-model="layout">
            <q-layout view="hHh lpR fFf" class="bg-white ventana">
                <q-page-container>

                    <h2>Comentarios sobre <span id="titulo">[ {{ titulo }} ]</span></h2>

                    <div v-if="!comentarios.length" >
                        "Esta noticia no tiene comentarios. Se el primero! (proximamente)."
                    </div>

                    <div id="comentario" v-for="comentario in comentarios" :key="comentario.code">
                        
                        <div class="q-gutter-y-md">   
                            <q-item v-ripple>
                                <q-item-section side>
                                    <q-avatar id="avatar" rounded color="purple" text-color="white">{{primeraLetra(comentario.autor)}}</q-avatar>
                                </q-item-section>
                                <q-item-section>
                                    <q-item-label>{{ comentario.autor }}</q-item-label>
                                    <q-item-label caption>{{ dateFormat(comentario.fecha) }}</q-item-label>
                                </q-item-section>
                            </q-item>
                        </div>

                        <!--<h3><span id="comt_autor">{{ comentario.autor }}</span> - {{ dateFormat(comentario.fecha) }}</h3>-->
                        <p>{{ comentario.texto }}</p>
                    </div>

                </q-page-container>
            </q-layout>
        </q-dialog>
    </div>
</template>

<script>
import axios from "axios";
import { dateFormat, primeraLetra } from "../assets/funciones";
import { ref } from 'vue'

export default {
    name: 'ComentarioList',
    setup() {
        return {
            layout: ref(false)
        }
    },
    data() {
        return {
            comentarios: [],
            
        };
    },
    props: {
        noticia: Number,
        titulo: String
    },
    methods: {
        dateFormat, primeraLetra,

        async getComentarios(noticia) {

            let url = "http://localhost:8000/api/noticias/" + noticia + "/comentarios/";
            let data = await axios.get(url)
            this.comentarios= data.data;
        }
    },

    created() {
        this.getComentarios(this.noticia);
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
    background-color: #d5dbaf;
}

#divbtn {
    text-align:right;
}

#btncomentario {
    background-color: #ffa726;
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