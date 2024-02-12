const { createApp } = Vue
// Create a toast
var notyf = new Notyf();
// let modal = document.getElementById('modalDatosPersonales')
// modal.style.display = 'none'

createApp({
    delimiters: ['[[', ']]'],
    data() {
        return {
            modal: null,

            // data del formulario de datos personales
            formNombreCompleto: '',
            formCarrera: '',
            formInstitucion: '',
            formEdad: '',
            formSemestreActual: '',
            formCorreoInstitucional: '',
            formAsignaturaFavorita: '',
            formEstadoEstudiante: '',
            formSexo: '',
            formOrientacionSexual: '',
            formBiografia: '',
            // data del formulario de datos personales
        }
    },


    methods: {
        modalDatosPersonales(val) {
            let modal = document.getElementById('modalDatosPersonales')
            modal.style.display = 'none'
            if (val) {
                fadeIn(modal)
            } else {
                fadeOut(modal)
            }

            function fadeOut(el) {
                el.style.opacity = 1;
                (function fade() {
                    if ((el.style.opacity -= 0.1) < 0) {
                        el.style.display = 'none'
                    } else {
                        requestAnimationFrame(fade)
                    }
                })()
            }

            function fadeIn(el, display) {
                el.style.opacity = 0
                el.style.display = display || 'block'
                    ; (function fade() {
                        let val = parseFloat(el.style.opacity)
                        if (!((val += 0.2) > 1)) {
                            el.style.opacity = val
                            requestAnimationFrame(fade)
                        }
                    })()
            }
        },

        cambiarDatosPersonales(event) {
            event.preventDefault()
            // console.log();
            // console.warn('formulario datos personales enviado')
            console.info('formulario datos personales enviado')

            const data = {
                'nombre_completo': this.formNombreCompleto,
                'carrera': this.formCarrera,
                'institucion': this.formInstitucion,
                'edad': this.formEdad,
                'semestre_cursado': this.formSemestreActual,
                'correo_institucional': this.formCorreoInstitucional,
                'asignatura_favorita': this.formAsignaturaFavorita,
                'estado_estudiante': this.formEstadoEstudiante,
                'sexo': this.formSexo,
                'orientacion_sexual': this.formOrientacionSexual,
                'biografia': this.formBiografia,
            }


            // TODO: verificar si todos los vmodel del formulario estan vacios, si lo estan mandar un return y dejar sin efecto la peticion axios.

            axios.post('http://127.0.0.1:8000/editar_datos_personales_perfil/', data)
                .then(response => {
                    console.log(response);

                    if (response.data.respuesta === 'success') {
                        // let modal = document.getElementById('modalDatosPersonales')
                        this.modal.style.display = 'none'
                        notyf.success('Datos actualizados correctamente.');
                    }

                    else if (response.data.respuesta === 'error') {
                        notyf.error('Ocurrio un error.');
                    }

                })
        },

        linksSelecionables() {
            console.log('link selecionado');
            // Obtener todos los elementos <a> con la clase "seleccionable"
            var links = document.querySelectorAll(".seleccionable");
            var pestaniaInformacionPersonal = document.getElementById('pestania-informacion-personal')
            var pestaniaPublicaciones = document.getElementById('pestania-publicaciones')


            // Añadir un event listener a cada enlace
            links.forEach(function (link) {
                link.addEventListener("click", function (event) {
                    // Evitar que el enlace actúe como un enlace normal
                    event.preventDefault();

                    // Desactivar la selección en todos los enlaces
                    links.forEach(function (enlace) {
                        enlace.classList.remove("seleccionado");

                        // div con de los paneles
                        pestaniaInformacionPersonal.classList.remove('pestaniaSeseleccionada')
                        pestaniaInformacionPersonal.classList.add('pestaniaDeseleccionada')
                        pestaniaPublicaciones.classList.remove('pestaniaSeseleccionada')
                        pestaniaPublicaciones.classList.add('pestaniaDeseleccionada')
                    });

                    // Activar la selección en el enlace actual
                    this.classList.add("seleccionado");
                    // console.log(this.id);
                    if (this.id === 'link-informacion-personal') {
                        pestaniaInformacionPersonal.classList.remove('pestaniaDeseleccionada')
                        pestaniaInformacionPersonal.classList.add('pestaniaSeleccionada')
                    }
                    
                    if (this.id === 'link-publicaciones') {
                        pestaniaPublicaciones.classList.remove('pestaniaDeseleccionada')
                        pestaniaPublicaciones.classList.add('pestaniaSeleccionada')
                        
                    }

                });
            });
        },




    },



    mounted() {
        // let modal = document.getElementById('modalDatosPersonales')
        this.modal = document.getElementById('modalDatosPersonales')
        this.modal.style.display = 'none'

        this.linksSelecionables()

    },
}).mount('#app')