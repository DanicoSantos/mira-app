<template>
  <div id="app" class="app">
    <Dashboard title="Dashboard"/>
  </div>
</template>

<script>
import Dashboard from './components/Dashboard.vue'

export default {
  name: 'App',
  components: {
    Dashboard
  }
}
</script>

<style>
.app {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
}

</style>
