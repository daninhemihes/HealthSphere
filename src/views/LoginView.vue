<template>
    <section class="content">
        <div class="forms">
            <img src="../assets/shadowLogo.png" alt="HealthSpaceLogo">
            <div id="wellcome-text">SEJA BEM-VINDO AO</div>
            <div id="logo-text">HEALTHSPACE</div>
            <SignInForm v-if="signType == 0"></SignInForm>
            <SignUpForm v-if="signType == 1"></SignUpForm>
        </div>
    </section>
  </template>
  
<script>
import SignInForm from '../components/SignForm/SignInForm.vue'
import SignUpForm from '../components/SignForm/SignUpForm.vue'

export default {
    name: 'LoginView',
    components: {
        SignInForm,
        SignUpForm,
    },
    data(){
        return{
            signType: 1,
        }
    }
}
</script>

<style scoped>
    .content{
        display: flex;
        flex-direction: row;
        justify-content: flex-end;

        background-image: url(../assets/nurseWallpaper.jpg);
    }
    .forms{
        height: 100vh;
        width: 630px;

        background: rgba(226, 226, 226, 0.5);
        backdrop-filter: blur(50px);
        -webkit-backdrop-filter: blur(50px);

        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .forms img{
        margin: 60px 0px 20px 0px;

        height: 130px;
        width: 130px;
    }
    .forms #wellcome-text{color: white; font-size: 24px; font-weight: 400;}
    .forms #logo-text{color: #236067; font-size: 34px; font-weight: 600;}

</style>
  