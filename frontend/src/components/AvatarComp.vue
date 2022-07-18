<template>
    <div class="q-gutter-y-md">
        <q-item v-ripple>
            <q-item-section side>
                <q-avatar id="avatar" rounded color="dorado" text-color="white">{{primeraLetra(nombre)}}</q-avatar>
            </q-item-section>
            <q-item-section>
                <q-item-label>{{ nombre }}</q-item-label>
                <q-item-label v-if="fecha!=undefined" caption>{{ fecha }}</q-item-label>
            </q-item-section>
        </q-item>
    </div>
</template>


<script>

import { primeraLetra } from "../assets/funciones";

export default {
    props: {
        nombre: String,
        fecha: String,
    },

    methods: {
        primeraLetra
    }, 
}

</script>

<style scoped>

#avatar {
    width: 48px !important;
    height: 48px !important;
}

</style>