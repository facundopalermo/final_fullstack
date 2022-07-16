<script setup>
import LoginForm from 'components/LoginForm.vue'
</script>

<template>
    <q-page class="row justify-center items-center" style="background: linear-gradient(#fffde7, #fff9c4);">
        <LoginForm></LoginForm>
    </q-page>

</template>

<script>
import { defineComponent } from 'vue'

export default defineComponent({
    name: 'LoginPage'
})
</script>