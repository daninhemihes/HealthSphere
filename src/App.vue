<template>
  <div class="app-container">
    <div class="side-nav">
      <NavBar/>
    </div>
    <div class="content">
      <router-view/>
    </div>
    
  </div>
</template>


<script>
  import NavBar from '@/components/NavBar.vue'

  export default {
  name: 'App',
  components: {
    NavBar
    }
  }
</script>

<style>
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    height: 100%;
  }
  html, body {
    margin: 0;
    height: 100%;
  }
  a {
    text-decoration: none;
    cursor: pointer;
  }

  .app-container {
    display: flex;
    flex-direction: row;
    width: 100%;
    height: 100%;
    overflow: hidden;

    background: linear-gradient(183.42deg, #235E65 4.92%, #0F282B 98.39%);
  }
  .side-nav {
    width: 100px;
    height: 100%;
  }
  .content {
    width: 100%;
    height: 100%;
    overflow: auto;

    background: #EEEEEE;
    border-radius: 30px 0px 0px 30px;
  }
</style>
