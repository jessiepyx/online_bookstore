import Vue from 'vue'
import Router from 'vue-router'
import Home from '../components/Home'
import Cart from '../components/Cart'
import Profile from '../components/Profile'
import History from '../components/History'
import BookDetail from '../components/BookDetail'
import Buy from '../components/Buy'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/cart',
      name: 'cart',
      component: Cart
    },
    {
      path: '/profile',
      name: 'profile',
      component: Profile
    },
    {
      path: '/history',
      name: 'history',
      component: History
    },
    {
      path: 'bookdetail/:id',
      name: 'bookdetail',
      component: BookDetail
    },
    {
      path: 'buy',
      name: 'buy',
      component: Buy
    }
  ]
})
