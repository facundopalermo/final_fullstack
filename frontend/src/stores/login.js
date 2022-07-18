import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'


export const useLoginStore = defineStore('login', {

	setup() {
		const router = useRouter();
	},

	state: () => ({
		autor: {
			estado: 0,
			id: 0,
			email: '',
			nombre: '',
			apellido: '',
			usuario: '',
			fecha_nac: '',
			last_login: '',
			date_joined: ''
		},

		HTTPstatus: 0
	}),

	getters: {
		Profile (state) {
			return state.autor
		}
	},

	actions: {
		async login (email, password) {

				const data = await axios.post('http://localhost:8000/login/', {     
					email: email,
					password: password,
		
				}, {
					withCredentials: false,
					headers: {
						'Content-Type': 'application/json',
					}
				}).catch((error) => {
					if(error.response){
						return error.response;
					}
				})

				if(data.status == 202) {
					this.autor.estado = 1
					this.autor.id = data.data.id
					this.autor.email = data.data.email
					this.autor.nombre = data.data.first_name
					this.autor.apellido = data.data.last_name
					this.autor.usuario = data.data.usuario
					this.autor.fecha_nac = data.data.fecha_nac
					this.autor.last_login = data.data.last_login
					this.autor.date_joined = data.data.date_joined
					this.HTTPstatus = data.status;
					sessionStorage.setItem('estado', 1)
					sessionStorage.setItem('email', email)
					sessionStorage.setItem('id', this.autor.id)
					sessionStorage.setItem('pass', password)
				} else {
					this.HTTPstatus = data.status;
				}
		},

		async registrar (first_name, last_name,	password, email, username, fecha_nac) {

			const data = await axios.post('http://localhost:8000/api/autores/', {
				first_name: first_name,
				last_name: last_name,
				password: password,
				email: email,
				username: username,
				fecha_nac: fecha_nac
			}, {
				headers: {
					'Content-Type': 'application/json',
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

		},
		logout(){
			axios.get('http://localhost:8000/logout/');
			this.$reset()
			sessionStorage.removeItem('estado')
			sessionStorage.removeItem('id')
			sessionStorage.removeItem('email')
			sessionStorage.removeItem('pass')
			this.router.push('/')
		  }
	}
})