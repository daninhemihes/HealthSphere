<template>
  <div class="home">
    <div class="banner">
      <div class="banner-title">
        <h2>Tenha Controle da</h2>
        <h2>Sua Saúde</h2>
      </div>
      <div class="banner-span">
        <h4></h4>
      </div>
      <div class="banner-button">
        <button @click="this.$router.push('/app/medicalrecord')">Ver Ficha Médica</button>
        <button @click="this.$router.push('/app/profileform')">Dados Pessoais</button>
        <button @click="this.$router.push('/app/medical')">Condições Médicas</button>
      </div>
    </div>
  </div>
</template>

<script>
import NavBar from '../components/NavBar.vue'


export default {
  name: 'HomeView',
  components: {
    NavBar
  }
}
</script>

<style>
  .home{
    display: flex;
    align-items: flex-end;
  }
  .banner{
    color: white;
    width: 100%;
    height: 60vh;

    background-image: url('../assets/nurseWallpaper.jpg');
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  .banner-button{
    display: flex;
  }
  .banner-button button{
    color: white;
    background: rgba(217, 217, 217, 0.4);
    border: 0.5px solid #C2C2C2;
    backdrop-filter: blur(10px);
    width: 34%;
    height: 150px;
  }
  .banner-title, .banner-span{
    margin: 50px;
  }

</style>
