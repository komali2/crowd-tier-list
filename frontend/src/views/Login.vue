<template>
  <div class="login">
    <label for="username">
      Username
      <input id="username" v-model="username" type="text">
    </label>
    <label for="password">
      Password
      <input id="password" v-model="password" type="password">
    </label>
    <div class="actions">
      <button
        @click="login"
      >Login</button>
      <button
        @click="register"
      >Register</button>
    </div>
  </div>
</template>

<script>

export default {
  name: 'Login',
  data() {
    return {
      username: '',
      password: '',
    };
  },
  mounted() {
  },
  methods: {
    login() {
      console.log('login with credentials', this.username, this.password);
    },
    register() {
      console.log('register with credentials', this.username, this.password);
    },
  },
};
</script>
<style scoped lang="scss">

.login {
  display: flex;
  flex-flow: column;
}
input {
  margin: 10px 0px;
}

button {
  font-size: 18px;
  margin: 10px 10px;
}

</style>
