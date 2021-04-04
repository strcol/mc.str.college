import Vue from 'vue';
import App from '@/components/App';

import BootstrapVue from 'bootstrap-vue';
import Vuelidate from 'vuelidate';

import 'bootstrap/dist/css/bootstrap.css';

Vue.use(BootstrapVue);
Vue.use(Vuelidate);

Vue.config.productionTip = false;

new Vue({
    render: h => h(App),
    data: {
        status: 0
    }
}).$mount('#app');
