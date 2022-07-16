import { defineStore } from 'pinia';
import axios from 'axios';

export const useNoticiaStore = defineStore("noticia", {
    state: () => ({
        todas: 0,
    }),

    getters: {},

    actions: {

        async getNoticias (id, orden) {

            let url = '';

            if(id === undefined) {
                url = 'http://localhost:8000/api/noticias/';
            } else {
                url = 'http://localhost:8000/api/autores/' + id + '/noticias/';
            }
            

            const data = await axios.get (url);

            if (data.status == 200) {
                this.todas = data.data;
                if(orden == 'asc'){
                    this.todas.reverse();
                }
            }
        }

    },
});
