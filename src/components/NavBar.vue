<template>
    <div class="nav-bar">
        <router-link to="/#" class="nav-logo">
            <i class="bi bi-heart-fill"></i>
        </router-link>
        <div class="nav-select">
            <router-link to="/#" active-class="nav-btn-active" class="nav-btn">
                <i class="bi bi-house-fill"></i>
            </router-link>

            <router-link to="/about" active-class="nav-btn-active" class="nav-btn">
                <i class="bi bi-clipboard-fill"></i>
            </router-link>

            <router-link to="/about" active-class="nav-btn-active" class="nav-btn">
                <i class="bi bi-activity"></i>
            </router-link>

            <router-link to="/about" active-class="nav-btn-active" class="nav-btn">
                <i class="bi bi-person-fill"></i>
            </router-link>

            <router-link to="/about" active-class="nav-btn-active" class="nav-btn">
                <i class="bi bi-gear-fill"></i>
            </router-link>
        </div>
        <div class="nav-end">
            <router-link to="/about" active-class="nav-btn-active" class="nav-btn">
                <i class="bi bi-box-arrow-in-left" style="font-size: 25px;"></i>
            </router-link>
        </div>
    </div>
</template>

<script >
export default {
  name: 'NavBar',

}
</script>

<style scoped>
.nav-bar{
    display: flex;
    flex-direction: column;
    justify-content: center;
    height: 100%;
}
.nav-logo{
    color: white;
    margin-top: 30px;
    font-size: 40px;
    flex-grow: 1;
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
    color: white;
    font-size: 20px;

    cursor: pointer;
    transition: 300ms;
}
.nav-btn-active{
    margin-left: 40px;
    width: 90px;
    padding-right: 30px;
    background-color: #EEEEEE;
    color: #235E65;
}
.nav-btn:hover{
    background-color:#235E65;
    color: white;
}
</style>
