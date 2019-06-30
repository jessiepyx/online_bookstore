import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)

export const store = new Vuex.Store({
  state: {
    bookItems: [],
    currentUser: JSON.parse(window.sessionStorage.getItem('user')),
    token: window.sessionStorage.getItem('token'),
    currentBook: null
  },
  getters: {
    // 获取属性的状态
  },
  mutations: {
    // 改变属性的状态
    changeUserMessage (state, data) {
      state.currentUser.email = data.email
      state.currentUser.telephone = data.telephone
      state.currentUser.imgUrl = data.imgUrl
    },
    setBookItems (state, data) {
      state.bookItems = data
    },
    setCurrentUser (state, data) {
      state.currentUser = data
      window.sessionStorage.setItem('user', JSON.stringify(data))
      console.log(JSON.parse(window.sessionStorage.getItem('user')))
    },
    setToken (state, data) {
      state.token = data
      window.sessionStorage.setItem('token', data)
    },
    logout (state) {
      state.token = null
      state.currentUser = null
      window.sessionStorage.removeItem('token')
      window.sessionStorage.removeItem('user')
    },
    setCurrentBook (state, data) {
      if (data != null) {
        state.currentBook = data
      } else {
        state.currentBook = null
      }
    }
  },
  actions: {
    // 应用mutations
  }
})
