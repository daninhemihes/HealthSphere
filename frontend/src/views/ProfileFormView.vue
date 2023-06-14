<template>
    <div class="profile-form">
        <label for="username">
            Primeiro Nome
            <input type="text" v-model="profileInfo.firstName">
        </label>
        <label for="email">
            Sobrenome
            <input type="text" v-model="profileInfo.lastName">
        </label>
        <label for="email">
            Sexo
            <select v-model="profileInfo.sex">
                <option disabled value="">Selecionar</option>
                <option value="F">Feminino</option>
                <option value="M">Masculino</option>
            </select>
        </label>
        <label for="email">
            Data de Nascimento
            <input type="date" v-model="profileInfo.birthDate">
        </label>
        <label for="email">
            Tipo Sanguíneo
            <select v-model="profileInfo.bloodType">
                <option disabled value="">Selecionar</option>
                <option>A+</option>
                <option>A-</option>
                <option>B+</option>
                <option>B-</option>
                <option>AB+</option>
                <option>AB-</option>
                <option>O+</option>
                <option>O-</option>
            </select>
        </label>
        <label for="email">
            Doador de Órgãos
            <input type="checkbox" v-model="profileInfo.organDonor">
        </label>
        <label for="email">
            Peso (kg)
            <input type="number" v-model="profileInfo.weight">
        </label>
        <label for="email">
            Altura (cm)
            <input type="number" v-model="profileInfo.height">
        </label>
        <label for="email">
            Estado Civil
            <input type="text" v-model="profileInfo.maritalStatus">
        </label>
        <label for="email">
            Cor
            <input type="text" v-model="profileInfo.color">
        </label>
        <label for="email">
            Nacionalidade
            <input type="text" v-model="profileInfo.nationality">
        </label>
        <label for="email">
            Profissão
            <input type="text" v-model="profileInfo.occupation">
        </label>
        <label for="email">
            Endereço
            <input type="text" v-model="profileInfo.address">
        </label>
        <label for="email">
            Telefone
            <input type="text" v-model="profileInfo.phone">
        </label>
        <label for="email">
            Linguagem Primária
            <input type="text" v-model="profileInfo.primaryLanguague">
        </label>
        <button @click="saveProfile()">SALVAR</button>
    </div>
</template>

<script>  
import ProfileService from '../services/profile'

export default {
    name: 'ProfileForm',
    components: {
    
},
data(){
    return{
        existingData: false,
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
async mounted() {
    const profileInfo = await ProfileService.getInfo(localStorage.getItem("username"))
    console.log(profileInfo)
    this.profileInfo = profileInfo
},
methods:{
    async saveProfile(){
        if(existingData){
            await ProfileService.updateInfo(localStorage.getItem("username"), this.profileInfo)
        }
        else {
            await ProfileService.setInfo(localStorage.getItem("username"), this.profileInfo)
        }
    }
}
}
</script>

<style>
.profile-form{
    display: flex;
    align-items: center;
    flex-direction: column;
}


</style>
