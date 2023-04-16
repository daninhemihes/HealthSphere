<template>
    <main id="app">
      <router-view/>
    </main>
</template>


<script>

  export default {
    name: 'App',
    components: {

    },
    data(){
      return{
        

      }
    }
  }

</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Lexend:wght@200;300;400;500;600;700&display=swap');

  #app {
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    height: 100vh;
    overflow: hidden;
    margin: 0;
    font-family: 'Lexend', sans-serif;
  }
  a {
    text-decoration: none;
    cursor: pointer;
  }
  /*
  .app-container {
    display: flex;
    flex-direction: row;

    overflow: hidden;

    background: linear-gradient(183.42deg, #235E65 4.92%, #0F282B 98.39%);
  }
  .side-nav {
    width: 100px;
    height: 100%;
  }
  */
  
</style>
