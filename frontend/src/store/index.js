import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    user: false,
  },
  getters: {
    isLoggedIn: (state) => !!state.user,
  },
  mutations: {
  },
  actions: {
    async getUsers() {
      const response = await fetch('api/');
      const responseJson = await response.json();
      console.log(responseJson);
    },
  },
  modules: {
  },
});

export default store;
