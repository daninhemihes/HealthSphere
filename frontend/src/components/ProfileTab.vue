<template>
    <div class="profiletab">
        <div v-if="!showEdit" class="profiletab-info">
            <div class="profileWelcome">
                <div class="profilePicture">
                    <i class="bi bi-person-fill"></i>
                </div>
                <div class="profileName">
                    Seja bem-vindo, {{ profileInfo.firstName }}!
                </div>
            </div>
            Resumo
            <div class="profileSummary">
                <div class="profileCard" style="background-color: blue;">
                    <div class="profileCardContainer">
                        <div class="profileCardTitle">
                            Peso
                        </div>
                        <div class="profileCardData">
                            {{ profileInfo.height }} Kg
                        </div>
                    </div>
                </div>
                <div class="profileCard" style="background-color: greenyellow;">
                    <div class="profileCardContainer">
                        <div class="profileCardTitle">
                            Altura
                        </div>
                        <div class="profileCardData">
                            {{ profileInfo.height / 100}} M
                        </div>
                    </div>
                </div>
                <div class="profileCard" style="background-color: red;">
                    <div class="profileCardContainer">
                        <div class="profileCardTitle">
                            Tipo Sanguíneo
                        </div>
                        <div class="profileCardData">
                            {{ profileInfo.bloodType}}
                        </div>
                    </div>
                </div>
                <div class="profileCard" style="background-color: skyblue;">
                    <div class="profileCardContainer">
                        <div class="profileCardTitle">
                            Doador de Órgãos
                        </div>
                        <div class="profileCardData">
                            {{ profileInfo.organDonor ? 'Sim' : 'Não'}}
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div v-else class="profiletab-edit">
            <button @click="this.$router.push('/app/profileform')">Configurar Perfil</button>
        </div>
    </div>
</template>

<script >
import ProfileService from '../services/profile'

export default {
    name: 'ProfileTab',
    data(){
        return{
            showEdit: true,
            profileInfo: {
                username: localStorage.getItem("username"),
                firstName : '',
                lastName : '',
                sex: '',
                birthDate: '',
                bloodType: '',
                organDonor: false,
                weight: 0.0,
                height: 0.0,
                maritalStatus : '',
                color : '',
                nationality : '',
                occupation : '',
                address : '',
                phone : '',
                primaryLanguague: ''
            }
        }
    },
    async mounted(){
        const profileInfo = await ProfileService.getInfo(localStorage.getItem("username"))
        if(profileInfo){
            this.showEdit = false
            this.profileInfo = profileInfo.data
        }
    },
    methods:{

    }
}
</script>

<style scoped>
.profiletab{
    display: flex;
    flex-direction: column;
    justify-content: center;
    height: 800px;
    width: 605px;
    background: #E2E2E2;
    padding: 30px;
}

.profiletab-info{
    font-family: 'Lexend';
    font-style: normal;
    font-weight: 400;
    font-size: 24px;
    line-height: 30px;
    color: #000000;
}
.profileWelcome{
    display: flex;
    flex-direction: row;
    margin: 0px 0px 40px 0px;
    align-items: center;
    justify-content: center;
}

.profilePicture{
    width: 90px;
    height: 90px;
    left: 1084px;
    top: 245px;
    background: #D9D9D9;
    margin-right: 40px;
    border-radius: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
}
.profilePicture i{
    color: white;
    font-size: 49px;
}

.profileSummary{
    display: flex;
    flex-direction: row;
    flex-grow: 3;
    justify-content: center;
    margin: 20px 0px;
    flex-wrap: wrap;
}

.profileCard{
    width: 176px;
    height: 107px;
    left: 1053px;
    top: 441px;
    margin: 15px;
    background: #00FF94;
    display: flex;
    align-items: end;
}
.profileCardContainer{
    width: 176px;
    height: 100px;
    left: 1053px;
    top: 441px;
    background: #FFFFFF;
    text-align: center;
}

.profileCardTitle{
    font-family: 'Lexend';
    font-style: normal;
    font-weight: 400;
    font-size: 18px;
    line-height: 22px;
    color: #606060;
}

.profileCardData{
    font-family: 'Lexend';
    font-style: normal;
    font-weight: 400;
    font-size: 32px;
    line-height: 40px;
    color: #010101;
}

</style>
