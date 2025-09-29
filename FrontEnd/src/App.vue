<template>
  <div id="app">
    <LoginForm />
  </div>
</template>

<script>
import LoginForm from './components/LoginForm.vue'

export default {
  name: 'App',
  components: {
    LoginForm
  }
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

#app {
  height: 100vh;
}
</style>
