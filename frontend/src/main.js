// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import axios from 'axios'
import App from './App'
import router from './router'
import {store} from './store'
import './plugins/element.js'

axios.defaults.baseURL = 'http://localhost:8080/online_bookstore'
Vue.prototype.$axios = axios

router.beforeEach((to, from, next) => {
  if (to.path === '/') {
    next()
  } else if (window.sessionStorage.getItem('token') === true) {
    next()
  } else {
    next(false)
  }
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
