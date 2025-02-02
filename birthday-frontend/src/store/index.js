import Vue from "vue";
import Vuex from "vuex";
import axios from 'axios';


Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    status: '',
    token: localStorage.getItem('token') || '',
    user : {},
  },
  mutations: {
    auth_request(state){
      state.status = 'loading'
    },
    auth_success(state, {token, user}){
      state.status = 'success'
      state.token = token
      state.user = user
    },
    auth_error(state){
      state.status = 'error'
    },
    logout(state){
      state.status = ''
      state.token = ''
    },
  },
  actions: {
    login({commit}, user){
      return new Promise((resolve, reject) => {
        commit('auth_request')
        axios({url: 'https://birthdayreminders-api.herokuapp.com/api/api-token-auth/', data: user, method: 'POST' })
        .then(resp => {
          const token = resp.data.token
          const user = resp.data.user_id
          localStorage.setItem('token', token)
          axios.defaults.headers.common['Authorization'] = "Token" + " " + token
          commit('auth_success', {token, user})
          resolve(resp)
        })
        .catch(err => {
          commit('auth_error')
          localStorage.removeItem('token')
          reject(err)
        })
      })
    },
    register({commit}, user){
      return new Promise((resolve, reject) => {
        commit('auth_request')
        axios({url: 'https://birthdayreminders-api.herokuapp.com/api/register/', data: user, method: 'POST'})
        .then(result => {
          if(result.status == 201){
            axios({url: 'https://birthdayreminders-api.herokuapp.com/api/api-token-auth/', data: user, method: 'POST' })
            .then(resp => {
              const token = resp.data.token
              const user = resp.data.user_id
              localStorage.setItem('token', token)
              axios.defaults.headers.common['Authorization'] = "Token" + " " + token
              commit('auth_success', {token, user})
              resolve(resp)
            })
            .catch(err => {
              commit('auth_error', err)
              localStorage.removeItem('token')
              reject(err)
            })
          }
        }).catch(err=> {
          commit('auth_error', err)
          console.log(err)
          reject(err)
        })
      })
    },
    logout({commit}){
      return new Promise((resolve) => {
        commit('logout')
        localStorage.removeItem('token')
        delete axios.defaults.headers.common['Authorization']
        resolve()
      })
    }
  },
  modules: {},
  getters : {
    isLoggedIn: state => !!state.token,
    authStatus: state => state.status,
    currUser: state => {return state.user},
  }
});
