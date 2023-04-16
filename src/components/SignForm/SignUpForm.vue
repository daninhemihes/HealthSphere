<template>
    <form action="">
        <label for="email">
            Nome Completo
            <input type="text">
        </label>
        <label for="email">
            E-mail
            <input type="text">
        </label>
        <label for="password">
            Senha
            <input type="password">
        </label>
        <button>CRIAR CONTA</button>
    </form>
    <div id="signup-btn">
        OU
        <button>CRIAR CONTA</button>
    </div>

  </template>
  
<script>

export default {
name: 'SignUpForm',
components: {

}
}
</script>

<style scoped>
    form{
        margin: 60px 0px 20px 0px;
        display: flex;
        flex-direction: column;
    }
    form label{
        display: flex;
        flex-direction: column;
        font-size: 20px;
        color: white;
        margin: 15px;
    }
    form input{
        width: 415px;
        height: 55px;
        background: none;
        color: white;
        border: 2px solid rgba(225, 225, 225, 0.8);
        filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.25));
        border-radius: 5px;
    }
    form label a{
        text-decoration: none;
        cursor: pointer;
        color: white;
        text-align: end;
        font-size: 16px;
    }
    form button, #signup-btn button{
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
    form button:hover, #signup-btn button:hover{
        font-size: 17px;
    }
    #signup-btn{
        display: flex;
        flex-direction: column;
        color: white;
        align-items: center;
    }

</style>
  