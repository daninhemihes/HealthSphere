<template>
    <div class="nav-bar">
        <router-link to="/#" class="nav-logo">
            <img src="../assets/logo.png" alt="Healthspace Logo" style="max-width: 60px;">
        </router-link>
        <div class="nav-select">
            <router-link to="/app/home" active-class="nav-btn-active" class="nav-btn">
                <i class="bi bi-house"></i>
            </router-link>

            <router-link to="/about" active-class="nav-btn-active" class="nav-btn">
                <i class="bi bi-clipboard"></i>
            </router-link>

            <router-link to="/app/medical" active-class="nav-btn-active" class="nav-btn">
                <i class="bi bi-lungs"></i>
            </router-link>

            <router-link to="/app/contacts" active-class="nav-btn-active" class="nav-btn">
                <i class="bi bi-people"></i>
            </router-link>

            <router-link to="/app/profileform" active-class="nav-btn-active" class="nav-btn">
                <i class="bi bi-person"></i>
            </router-link>
        </div>
        <div class="nav-end">
            <router-link @click="logout()" to="/" active-class="nav-btn-active" class="nav-btn">
                <i class="bi bi-box-arrow-in-left" style="font-size: 25px;"></i>
            </router-link>
        </div>
    </div>
</template>

<script >
export default {
  name: 'NavBar',
  methods:{
    logout(){
        localStorage.setItem('username', '')
    }
  }

}
</script>

<style scoped>
.nav-bar{
    display: flex;
    flex-direction: column;
    justify-content: center;
    height: 800px;
    width: 110px;
    background: #E2E2E2;
}
.nav-logo{
    color: #236067;
    margin-top: 30px;
    font-size: 40px;
    flex-grow: 1;
    text-align: center;
}
.nav-select{
    display: flex;
    flex-direction: column;
    flex-grow: 1;
    align-items: center;
}
.nav-end{
    display: flex;
    flex-direction: column;
    flex-grow: 1;
    align-items: center;
}

.nav-btn{
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 10px;
    height: 50px;
    width: 50px;
    margin: 10px;
    color: #236067;
    font-size: 25px;
    font-weight: 300;

    cursor: pointer;
    transition: 300ms;
}
.nav-btn-active{
    margin-left: 40px;
    width: 90px;
    padding-right: 30px;
    background-color: #EEEEEE;
    color: #236067;
}
.nav-btn:hover{
    background-color:#236067;
    color: #EEEEEE;
}
</style>
