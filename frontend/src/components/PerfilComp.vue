<template>
        <q-card class="my-card" v-if="ver">
            <q-card-section>
                <div class="text-h6">Hola!! {{perfil.nombre}} {{perfil.apellido}}</div>
                <div class="text-subtitle2 padding">Estos son tus datos:</div>
                
                <div  class="shadow-2 rounded-borders padding">
                    <div class="text-subtitle2">Fecha de nacimiento: {{perfil.fecha_nac}}</div>
                    <div class="text-subtitle2">Email: {{perfil.email}}</div>
                    <div class="text-subtitle2">Último Login: {{dateFormat(perfil.last_login)}}</div>
                    <div class="text-subtitle2">Dia en que te uniste: {{dateFormat(perfil.date_joined)}}</div>
                </div>

            </q-card-section>

            <q-tabs v-model="tab" class="text-teal">
                <q-tab label="Noticias" name="noticiasTab" />
                <q-tab label="Comentarios" name="comentariosTab" />
            </q-tabs>

            <q-separator />

            <q-tab-panels v-model="tab" animated>
                <q-tab-panel name="noticiasTab">
                    <div class="q-pa-md ">
                        <q-table
                            :rows="notiRows"
                            :columns="notiColumns"
                            row-key="code"
                            no-data-label="No tienes noticias publicadas!"
                        >
                        <template v-slot:body-cell-delete="cellProperties">
                            <q-td :props="cellProperties">
                                <q-btn round color="red" glossy text-color="black" icon="delete_forever" @click="borrarNoti(cellProperties.value)"/>
                            </q-td>
                        </template>
                        
                        </q-table>
                    </div>
                </q-tab-panel>

                <q-tab-panel name="comentariosTab">
                    <div class="q-pa-md ">
                        <q-table
                            :rows="comentRows"
                            :columns="comentColumns"
                            row-key="code"
                            no-data-label="No tienes comentarios realizados!"
                            >
                            <template v-slot:body-cell-delete="cellProperties">
                                <q-td :props="cellProperties">
                                    <q-btn round color="red" glossy text-color="black" icon="delete_forever" @click="borrarComentario(cellProperties.value)"/>
                                </q-td>
                            </template>
                        </q-table>
                    </div>
                </q-tab-panel>
            </q-tab-panels>
        </q-card>
        <div v-else>Acceso no autorizado a esta sección. Primero inicie sesión.</div>
</template>

<script>
import { useLoginStore } from 'src/stores/login';
import { dateFormat } from '../assets/funciones';
import { ref } from 'vue'
import axios from 'axios'

const notiColumns = [
    {
        name: 'code',
        label: 'Código',
        align: 'left',
        field: 'code',
        sortable: true,
        style: 'max-width: 10px;'
    },
        { name: 'titulo', align: 'left', label: 'Título', field: 'titulo', sortable: true},
        { name: 'fecha', align: 'left', label: 'Fecha', field: 'fecha', sortable: true, format: val=>new Date(`${val}`).toLocaleDateString('es-ES', {hour: 'numeric', minute: 'numeric'})},
        { name: 'delete', align: 'center', label: 'Borrar', field: 'code', sortable: false},
    ]

const comentColumns = [
    {
        name: 'code',
        label: 'Código',
        align: 'left',
        field: 'code',
        sortable: true,
    },
        { name: 'texto', align: 'left', label: 'Comentario', field: 'texto', sortable: true},
        { name: 'noticia', align: 'left', label: 'Noticia', field: 'noticia', sortable: true},
        { name: 'fecha', align: 'left', label: 'Fecha', field: 'fecha', sortable: true, format: val=>new Date(`${val}`).toLocaleDateString('es-ES', {hour: 'numeric', minute: 'numeric'})},
        { name: 'delete', align: 'center', label: 'Borrar', field: 'code', sortable: false},
    ]

export default {

    setup() {
        const datos = useLoginStore();
        const perfil = datos.autor;

        return {
            perfil,
            tab: ref('noticiasTab'),
            notiColumns,
            comentColumns,
        }
    },
    data() {
        return {
            notiRows: [],
            comentRows: []
        }
    },

    components: {
        
    },

    computed: {
        ver() {
            if(sessionStorage.getItem('estado')==1){
                return true;
            }else{
                return false;
            }
        }
    },

    methods: {
        dateFormat,
        async getNoticias () {

            let url = 'http://localhost:8000/api/autores/' + sessionStorage.getItem('id') + '/noticias/';

            const data = await axios.get(url);

            if (data.status == 200) {
                this.notiRows = data.data;
            }
        },

        async getComentarios () {

            let url = 'http://localhost:8000/api/autores/' + sessionStorage.getItem('id') + '/comentarios/';

            const data = await axios.get(url);

            if (data.status == 200) {
                this.comentRows = data.data;
            }
        },
        async borrarNoti (noticia) {

            if(confirm('Está seguro de eliminar la noticia?')){
                let url = 'http://localhost:8000/api/noticias/' + noticia;

                const data = await axios.delete(url);

                if (data.status == 204) {
                    await this.getNoticias();
                }
            }
            
        },
        async borrarComentario (comentario) {

            if(confirm('Está seguro de eliminar la noticia?')){
                let url = 'http://localhost:8000/api/comentarios/' + comentario;

                const data = await axios.delete(url);

                if (data.status == 204) {
                    await this.getComentarios();
                }
            }
        }
    }, 

    watch: {
        
    },

    async created() {
        await this.getNoticias();
        await this.getComentarios();
    },
        
};
</script>

<style>

.padding {
    padding:10px;
}
.q-table thead th {
    white-space: normal;
}

.q-table tbody td {
    white-space: normal;
    max-width: 660px;
}

</style>

<style lang="sass" scoped>
.full-width
    width: 100%

.my-card
    width: 100%
    max-width: 1000px

.noti_texto
    text-align: justify

a
    color: white

.text-h4
    color: #deb03f

</style>