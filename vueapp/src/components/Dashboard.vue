<template>
  <div class="dashboard">
    <h1 class="dashboard__title">{{ title }}</h1>
    <button v-on:click="reverseTitle">Reverse Title</button>
  </div>
  
</template>

<script>
export default {
  name: 'Dashboard',
  props: {
      title: String
  },
  methods: {
    reverseTitle: function() {
      this.title = this.title.split('').reverse().join('')
    }
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.dashboard {
    font-family: 'Poppins', sans-serif;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    width: 100%;
}

.dashboard__title {
    text-transform: uppercase;
}

</style>
