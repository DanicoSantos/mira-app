let app = new Vue({
    el: '#app',
    data() {
        return {
            info: null
        }
    }, 
    mounted() {
        axios.get('https://statusinvest.com.br/acoes/busca-avancada')
        .then(reponse => (console.log(response)))
    }
});