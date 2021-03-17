<template>
  <div class="login">
    <label for="username">
      <input id="username" v-model="username" type="text">
    </label>
    <label for="password">
      <input id="password" v-model="password" type="password">
    </label>
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
};
</script>
