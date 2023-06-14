<template>
    <div class="loginForm">
        <label for="username">
            Usuário
            <input type="text" v-model="username">
        </label>
        <label for="email">
            E-mail
            <input type="text" v-model="email">
        </label>
        <label for="password">
            Nova Senha
            <input type="password" v-model="password">
        </label>
        <button @click="createAccount()"> CRIAR CONTA</button>
        <div id="signup-btn">
            OU
            <button @click="$emit('changeForm')">FAZER LOGIN</button>
        </div>
    </div>

  </template>
  
<script>
import user from '../../services/user'
import UserService from '../../services/user'

export default {
    name: 'SignUpForm',
    components: {

    },
    data(){
        return{
            username: '',
            email: '',
            password: ''
        }
    },
    methods:{
        async createAccount () {
            const response = await UserService.register(this.username, this.email, this.password)
            if (response && response.status == 201){
                localStorage.setItem("username", this.username)
                alert(`Usuário ${localStorage.getItem("username")} registrado!`)
                this.$router.push("/app/home")
            }
            else{
                alert('Não foi possível registrar o usuário.')
            }
        }
    }
}
</script>

<style scoped>
    .loginForm{
        margin: 60px 0px 20px 0px;
        display: flex;
        flex-direction: column;
    }
    .loginForm label{
        display: flex;
        flex-direction: column;
        font-size: 20px;
        color: white;
        margin: 15px;
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
        margin: 15px;
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
  