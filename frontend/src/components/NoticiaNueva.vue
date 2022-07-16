<template>
<q-page-sticky position="bottom-right" :offset="[18, 18]" v-if="loginStore.autor.estado==1">
    <q-btn fab icon="add" color="amber" class="inset-shadow-down">
        <q-tooltip class="bg-amber text-black shadow-4" :offset="[10, 10]">
            Agregar Noticia
        </q-tooltip>
    </q-btn>
</q-page-sticky>


</template>

<script>

import { useLoginStore } from 'src/stores/login'

export default {
    setup() {
        const loginStore = useLoginStore();
        return {
            loginStore
        }
    }
}

</script>