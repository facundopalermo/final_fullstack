<template>
    <q-page class="row justify-center items-center" style="background: linear-gradient(#fffde7, #fff9c4);">
        <perfil-comp></perfil-comp>
    </q-page>

</template>

<script>
import { defineComponent } from 'vue'
import PerfilComp from 'components/PerfilComp.vue'

export default defineComponent({
    name: 'PerfilPage',

    components: {
        PerfilComp,
    }
})
</script>