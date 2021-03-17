import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
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
