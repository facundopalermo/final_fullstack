<template>
  <q-layout view="hHh lpR fFf">

    <q-header elevated class="bg-dark text-white" height-hint="98">
      <q-toolbar>
        <q-toolbar-title>
          <q-avatar>
            <img src="../assets/logo.svg">
          </q-avatar>
          Noticias Doradas
        </q-toolbar-title>
      </q-toolbar>

      <q-tabs align="left">
        <q-route-tab to="/" label="Portada" />
        <q-route-tab to="/login" label="Iniciar sesión" v-if="loginStore.autor.estado==0"/>
        <q-route-tab v-on:click="logout()" label="LogOut" v-else/>
      </q-tabs>
    </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>

    <q-footer elevated class="bg-dark text-white">
      <q-toolbar>
        <q-toolbar-title class="foot">
          <div>Facundo Esteban Palermo - Universidad de Palermo - Fullstack Web Development</div>
        </q-toolbar-title>
      </q-toolbar>
    </q-footer>

  </q-layout>
</template>

<script>
import { defineComponent } from 'vue'
import { useLoginStore } from 'src/stores/login'
import axios from 'axios';


export default defineComponent({
  name: 'MainLayout',

  setup() {

    const loginStore = useLoginStore();

    return {
      loginStore
    }
  },

  components: {
  },

  methods: {
    logout(){
      axios.get('http://localhost:8000/logout/');
      this.loginStore.$reset();
    }
  }

})
</script>

<style>
.q-avatar {
  height: 100px;
  width: 100px;
}

.q-toolbar__title {
  font-size: 50px;
  color: #ffa726
}

.foot {
  font-size: 15px;
  color: white
}

</style>
