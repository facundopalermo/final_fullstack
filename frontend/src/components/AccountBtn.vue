<template>
    <div class="q-pa-md">
        <q-btn style="background-color: #deb03f; color:black;" :label="loginStore.autor.nombre">
            <q-menu>
                <div class="row no-wrap q-pa-md">

                    <div class="column items-center">
                        <div class="text-h6 q-mb-md">Cuenta</div>
                        <q-btn flat style="color: #deb03f" label="Administrar" to="/perfil"/>
                    </div>

                    <q-separator vertical inset class="q-mx-lg" />

                    <div class="column items-center">
                        <q-avatar id="avatar" rounded color="dorado" text-color="white">
                            {{primeraLetra(loginStore.autor.nombre)}}</q-avatar>
                        <div class="text-subtitle1 text-center q-mt-md q-mb-xs items-center">{{loginStore.autor.nombre}} {{loginStore.autor.apellido}}</div>
                        <q-btn color="dark" label="Logout" size="sm" v-close-popup v-on:click="loginStore.logout()" />
                    </div>
                </div>
            </q-menu>
        </q-btn>
    </div>
</template>


<script>

import { primeraLetra } from "../assets/funciones";
import { useLoginStore } from 'src/stores/login'

export default {

    setup() {
        const loginStore = useLoginStore();
        return {
            loginStore
        }
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