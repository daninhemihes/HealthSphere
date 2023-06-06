<template>
    <div class="nav-bar">
        I am a profile tab
    </div>
</template>

<script >
export default {
  name: 'ProfileTab',

}
</script>

<style scoped>
.nav-bar{
    display: flex;
    flex-direction: column;
    justify-content: center;
    height: 800px;
    width: 605px;
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
