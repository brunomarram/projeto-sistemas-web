import * as Vue from 'vue'
import App from './App.vue'
import * as Buefy from 'buefy'
// import 'buefy/dist/buefy.css'

import responsive from 'vue-responsive'

import router from './router'

Vue.createApp(App)
    .use(router)
    .use(Buefy)
    .use(responsive)
    .mount('#app')
  
