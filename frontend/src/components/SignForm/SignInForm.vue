<template>
    <div class="loginForm">
        <label for="username">
            Usuário
            <input v-model="username" type="text">
        </label>
        <label for="password">
            Senha
            <input v-model="password" type="password">
            <!-- <a href="">Esqueci minha senha</a> -->
        </label>
        <button @click="login()">FAZER LOGIN</button>
        <div id="signup-btn">
            OU
            <button @click="$emit('changeForm')">CRIAR CONTA</button>
        </div>
      </div>
  </template>
<script>
import UserService from '../../services/user'

export default {
name: 'SignInForm',
components: {

},
data() {
    return {
      username: '',
      password: ''
    };
  },
  methods: {
    async login() {
      try {
        const response = await UserService.login(this.username, this.password)
            if (response && response.status == 200){
              console.log(response)
                localStorage.setItem("username", this.username)
                this.$router.push("/app/home")
            }
            else{
                alert('Usuário ou senha incorretos.')
            }
      } catch (error) {
        console.error('Erro ao fazer login:', error);
      }
    }
  }
}
</script>

<style scoped>
    .loginForm{
        margin: 120px 0px 20px 0px;
        display: flex;
        flex-direction: column;
    }
    .loginForm label{
        display: flex;
        flex-direction: column;
        font-size: 20px;
        color: white;
        margin: 20px;
    }
    .loginForm input{
        width: 415px;
        height: 55px;
        background: none;
        color: white;
        border: 2px solid rgba(225, 225, 225, 0.8);
        filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.25));
        border-radius: 5px;
    }
    .loginForm label a{
        text-decoration: none;
        cursor: pointer;
        color: white;
        text-align: end;
        font-size: 16px;
    }
    .loginForm button, #signup-btn button{
        width: 415px;
        height: 60px;
        margin: 20px;
        background: linear-gradient(112.07deg, #79B4AE 33.17%, #699E97 68.77%);
        border: 1px solid #3E7479;
        border-radius: 10px;
        color: white;
        font-size: 20px;
        transition: 0.2s;
    }
    .loginForm button:hover, #signup-btn button:hover{
        font-size: 17px;
    }
    #signup-btn{
        display: flex;
        flex-direction: column;
        color: white;
        align-items: center;
    }

</style>
  