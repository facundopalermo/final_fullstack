import { defineStore } from 'pinia';
import axios from 'axios';

export const useNoticiaStore = defineStore("noticia", {
    state: () => ({
        todas: 0,
        HTTPstatus: 0
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
                this.todas = data.data.reverse();
                if(orden === undefined || orden == 'asc'){
                    this.todas.reverse();
                }
                if(id !== undefined) {
                    this.todas.reverse();
                }
            }
        },
        async noticiaNueva (titulo, texto, autor) {

			const data = await axios.post('http://localhost:8000/api/noticias/', {
				titulo: titulo,
				texto: texto,
				fecha: new Date().toISOString(),
                autor_id: autor
			}, {
				withCredentials: false,
				headers: {
						'Content-Type': 'application/json',
                        'accept': 'application/json',
				}
			}).catch((error) => {
				if(error.response) {
					console.log(error.message)
					return error.response.status;
				}
			})

			if(data.status == 201) {
                this.HTTPstatus = 201;
			} else {
				this.HTTPstatus = 400;
            }

            this.getNoticias();
		},

    },
});
