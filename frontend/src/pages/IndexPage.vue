<template>
    <q-page class="column items-center">
        <noticia-list></noticia-list>
        <noticia-nueva></noticia-nueva>
    </q-page>
</template>

<script>
import { defineComponent } from 'vue'
import NoticiaList from '../components/NoticiaList.vue'
import NoticiaNueva from '../components/NoticiaNueva.vue'

export default defineComponent({
    name: "IndexPage",
    components: { NoticiaList, NoticiaNueva },

    
})
</script>
