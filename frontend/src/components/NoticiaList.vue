<template>
    <div class="q-pa-md bg-grey-9 text-white row justify-center" style="width: 100%;">
        <div class="q-gutter-sm">
            <q-radio dark v-model="shape" val="asc" label="Más nuevos primero" v-on:click="ordenar(shape)" />
            <q-radio dark v-model="shape" val="desc" label="Más antiguos primero" v-on:click="ordenar(shape)"/>
            <q-btn outline style="color: goldenrod;" label="Recargar" v-on:click="reset()"/>
        </div>
    </div>

    <div v-for="noticia in noticias" :key="noticia.code" style="width: 100%;" class="q-pa-md row items-start justify-center">
            <q-card dark bordered class="bg-grey-9 my-card">
                <q-card-section style="width: 100%">
                    <div class="text-subtitle3">{{ dateFormat(noticia.fecha) }}</div>
                    <div class="text-h4">{{ noticia.titulo }}</div>
                    <div class="text-subtitle2">por <a :href="'/#/' + noticia.autor_id +'/'">{{ noticia.autor }}</a></div>
                    
                </q-card-section>

                <q-separator dark inset />

                <q-card-section class="noti_texto"> {{ noticia.texto }} </q-card-section>
                <ComentarioList :noticia="noticia.code" :titulo="noticia.titulo"></ComentarioList>
            </q-card>
    </div>
</template>

<script>
import { useNoticiaStore } from 'src/stores/noticia';
import { useLoginStore } from 'src/stores/login';
import { dateFormat } from '../assets/funciones';
import ComentarioList from 'components/ComentarioList.vue';
import { ref } from 'vue';


export default {

    setup() {
        const noticiaStore = useNoticiaStore();
        const loginStore = useLoginStore();

        return {
            noticiaStore,
            shape: ref('asc'),
            loginStore,
        }
    },

    components: {
        ComentarioList,
    },

    created() {

        this.noticiaStore.getNoticias(this.$route.params.id, this.$route.params.orden);
    },

    methods: {
        dateFormat,
        ordenar(orden){
            this.$router.push({query: {orden: orden}});
        },
        reset(){
            this.$router.push('/');
        }
    }, 

    watch: {
        '$route.params.id' () {
            this.noticiaStore.getNoticias(this.$route.params.id);
        },
        '$route.query.orden' () {
            this.noticiaStore.getNoticias(this.$route.params.id, this.$route.query.orden);
            this.shape = ref(this.$route.query.orden)
        }
    },
    computed: {
        noticias () {
            return this.noticiaStore.todas;
        }
    }
        
};
</script>

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