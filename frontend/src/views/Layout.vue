<template>
    <div class="layout">
      <NavBar></NavBar>
      <div class="content">
        <router-view/>
      </div>
      <ProfileTab></ProfileTab>
    </div>
  </template>
  
  <script>
  import NavBar from '../components/NavBar.vue'
  import ProfileTab from '../components/ProfileTab.vue';
  
  export default {
    name: 'Layout',
    components: {
      NavBar,
      ProfileTab
    },
    mounted() {
      const username = localStorage.getItem("username")
      if (!username || username == '') this.$router.push("/")
  },
  }
  </script>
  
  <style scoped>
    .layout{
        display: flex;
        height: 100vh;
        align-items: flex-end;
        background-image: url('../assets/nurseWallpaperBlur.png');
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
    }
    .content{
        flex-grow: 1;
        height: 90vh;
        background: white;
    }
  </style>
  