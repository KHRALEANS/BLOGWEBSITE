<template>
  <div id="app">
    <Navbar />
    <div class="container mt-5 mb-5">
      <router-view />
    </div>

  </div>
</template>

<script>

import Navbar from "@/components/Navbar";



export default {
  name: 'App',
  components: {

    Navbar,

  },
  data() {
    return {

    }
  }
}
</script>

<style>

</style>
