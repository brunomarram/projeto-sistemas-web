import Vue from 'vue'
import App from './App.vue'

import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'

import VueRouter from 'vue-router'
import router from './router'

Vue.use(VueRouter);
Vue.use(VueMaterial);

Vue.config.productionTip = false

new Vue({ router, render: h => h(App) }).$mount('#app')