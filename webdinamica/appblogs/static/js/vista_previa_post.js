const { createApp } = Vue
// Create a toast
// var notyf = new Notyf();
// let modal = document.getElementById('modalDatosPersonales')
// modal.style.display = 'none'
// import { Confirm } from '../../../static/js/notiflix-Notiflix-78ca6fa/dist/';
// import { Confirm } from 'notiflix/build/notiflix-confirm-aio';

Notiflix.Confirm.init({
    borderRadius: '7px',
    titleColor: 'black',
    okButtonBackground: '#1B75D0',
    cancelButtonBackground: '#EC4444'

})


createApp({
    delimiters: ['[[', ']]'],
    data() {
        return {
            mensaje: 'Hola, Mundo desde Vue.js'
        }
    },


    methods: {
        opcionEliminarPost(event) {
            console.log(event.target.id);
            Notiflix.Confirm.show(
                'Eliminar Post',
                '¿Estás seguro de que quieres eliminar este post?',
                'Si',
                'No',
                function okCb() {
                    axios.post(`http://127.0.0.1:8000/blogs/eliminar_post/${event.target.id}`, {id_post: event.target.id})
                        .then(response => {
                            console.log(response.data);
                            
                            if (response.data.respuesta) {
                                window.location.href = `http://127.0.0.1:8000/`
                            }
                    })
                    // alert('Thank you.');
                },
                function cancelCb() {
                    // alert('If you say so...');
                },
                {
                },
            );
        }
    }



}).mount('#app')
