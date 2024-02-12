const { createApp } = Vue

createApp({
    delimiters: ['${', '}'],
    data() {
        return {
            nombreUsuario: '',
            correoElectronico: '',
            contrasenia: '',
            repetirContrasenia: ''
        }
    },

    methods: {
        verificarDatosRegistro(event) {
            event.preventDefault()

            if (this.contrasenia === this.repetirContrasenia) {
                const data = {
                    nombreUsuario: this.nombreUsuario,
                    correoElectronico: this.correoElectronico,
                    contrasenia: this.contrasenia
                }

                axios.post('http://127.0.0.1:8000/crear_cuenta/', data)
                    .then(response => {
                        console.log(response);

                        if (response.data.estado === 'success') {
                            window.location.href = `http://127.0.0.1:8000/`
                            // console.log(response);
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
            }
            else {
                var notyf = new Notyf({
                    duration: 4000,
                    position: {
                        x: 'right',
                        y: 'bottom',
                    },
                })
                notyf.error({
                    message: 'Las contraseñas no coinciden.',
                    dismissible: true,
                    ripple: true,
                })
            }


        }


    }


}).mount('#app')