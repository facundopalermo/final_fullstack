<template>
    <q-page class="column items-center" style="background: linear-gradient(#fffde7, #fff9c4);">
        <noticia-list></noticia-list>
        <noticia-nueva></noticia-nueva>
        <q-page-scroller expand position="top" :scroll-offset="150" :offset="[0, 0]">
            <div class="col cursor-pointer q-pa-sm bg-dorado text-black-bold text-weight-bolder text-center">
                <q-icon name="arrow_upward" class="text-black text-weight-bolder" size="2em" />
                ir al arriba...
            </div>
        </q-page-scroller>
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
