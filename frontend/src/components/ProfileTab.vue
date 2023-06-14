<template>
    <div class="profiletab">
        <div v-if="!showEdit" class="profiletab-info">

        </div>
        <div v-else class="profiletab-edit">
            <button @click="this.$router.push('/app/profileform')">Configurar Perfil</button>
        </div>
    </div>
</template>

<script >
export default {
    name: 'ProfileTab',
    data(){
        return{
            showEdit: true,
            profileInfo: {
                username: '',
                firstName : '',
                lastName : '',
                sex: '',
                birthDate: '',
                bloodType: '',
                organDonor: '',
                weight: '',
                height: '',
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
    mounted(){

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
}

</style>
