const { createApp } = Vue

createApp({
    delimiters: ['${', '}'],
    data() {
        return {
            nombreUsuario: '',
            contrasenia: '',
        }
    },

    methods: {
        verificarDatosLogin(event) {
            event.preventDefault()

            const data = {
                nombreUsuario: this.nombreUsuario,
                contrasenia: this.contrasenia
            }

            axios.post('http://127.0.0.1:8000/crear_sesion/', data)
                .then(response => {
                    console.log(response);
                    // window.location.href = `http://127.0.0.1:8000/main/inicio/` || 'https://zn87zdp0-8000.brs.devtunnels.ms/main/inicio'
                    window.location.href = 'https://zn87zdp0-8000.brs.devtunnels.ms/main/inicio'

                    if (response.data.estado === 'success') {
                        console.log(response);
                    }

                    else if (response.data.estado === 'error') {
                        var notyf = new Notyf({
                            duration: 4000,
                            position: {
                                x: 'right',
                                y: 'bottom',
                            },
                        })
                        notyf.error({
                            message: response.data.mensaje,
                            dismissible: true,
                            ripple: true,
                        })
                    }
                })
                .catch(error => {
                    console.log(error);
                })
            // else {
            //     var notyf = new Notyf({
            //         duration: 4000,
            //         position: {
            //             x: 'right',
            //             y: 'bottom',
            //         },
            //     })
            //     notyf.error({
            //         message: 'Las contraseñas no coinciden.',
            //         dismissible: true,
            //         ripple: true,
            //     })
            // }


        }


    }


}).mount('#app')