<template>
    <div class="container">
        <div class="text">
            Seu Perfil
        </div>
        <form action="#">
            <div class="form-row">
                <div class="input-data">
                    <input type="text" v-model="profileInfo.firstName" required>
                    <div class="underline"></div>
                    <label for="">Primeiro Nome</label>
                </div>
                <div class="input-data">
                    <input type="text" v-model="profileInfo.lastName" required>
                    <div class="underline"></div>
                    <label for="">Sobrenome</label>
                </div>
                <div class="input-data">
                    <input type="date" v-model="profileInfo.birthDate" required>
                    <div class="underline"></div>
                    <label for="">Data de Nascimento</label>
                </div>
                <div class="input-data">
                    <input type="text" v-model="profileInfo.color" required>
                    <div class="underline"></div>
                    <label for="">Cor</label>
                </div>
            </div>
            <div class="form-row">
                <div class="input-data">
                    <input type="number" v-model="profileInfo.weight" required>
                    <div class="underline"></div>
                    <label for="">Peso</label>
                </div>
                <div class="input-data">
                    <input type="number" v-model="profileInfo.height" required>
                    <div class="underline"></div>
                    <label for="">Altura</label>
                </div>
                <div class="input-data">
                    <input type="text" v-model="profileInfo.primaryLanguague" required>
                    <div class="underline"></div>
                    <label for="">Idioma</label>
                </div>
                <div class="input-data">
                    <input type="text" v-model="profileInfo.address" required>
                    <div class="underline"></div>
                    <label for="">Endereço</label>
                </div>
            </div>
            <div class="form-row">
                <div class="input-data">
                    <input type="text" v-model="profileInfo.maritalStatus" required>
                    <div class="underline"></div>
                    <label for="">Estado Civil</label>
                </div>
                <div class="input-data">
                    <input type="text" v-model="profileInfo.phone" required>
                    <div class="underline"></div>
                    <label for="">Telefone</label>
                </div>
                <div class="input-data">
                    <input type="text" v-model="profileInfo.nationality" required>
                    <div class="underline"></div>
                    <label for="">Nacionalidade</label>
                </div>
                <div class="input-data">
                    <input type="text" v-model="profileInfo.occupation" required>
                    <div class="underline"></div>
                    <label for="">Profissão</label>
                </div>
            </div>
            <div class="form-row">
                <div class="input-data">
                    <input type="checkbox" v-model="profileInfo.organDonor" required>
                    <div class=""></div>
                    <label for="">Doador de Órgãos</label>
                </div>
                <div class="input-data">
                    <div for="">Sexo</div>
                    <select v-model="profileInfo.sex">
                        <option disabled value="">Sexo</option>
                        <option value="F">Feminino</option>
                        <option value="M">Masculino</option>
                    </select>
                </div>
                <div class="input-data">
                    <div for="">Tipo Sanguíneo</div>
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
                    <div class="underline"></div>
                </div>
                <div class="input-data">
                    <div class="inner"></div>
                    <input type="submit" value="Salvar" @click="saveProfile()">
                </div>
            </div>
        </form>
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
    if(profileInfo){
        this.existingData = true
        this.profileInfo = profileInfo.data
    }
},
methods:{
    async saveProfile(){
        if(this.existingData){
            console.log(this.profileInfo)
            await ProfileService.updateInfo(localStorage.getItem("username"), this.profileInfo)
            alert('Dados atualizados!')
            this.$router.push("/")
        }
        else {
            await ProfileService.setInfo(localStorage.getItem("username"), this.profileInfo)
            alert('Dados adicionados!')
            this.$router.push("/")
        }
    }
}
}
</script>

<style scoped>
.profile-form{
    display: flex;
    align-items: center;
    flex-direction: column;
}

.container{
  background: #fff;
  padding: 25px 40px 10px 40px;
  box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
}
.container .text{
  text-align: center;
  font-size: 41px;
  font-weight: 600;
  font-family: 'Poppins', sans-serif;
  background: -webkit-linear-gradient(112.07deg, #79B4AE 33.17%, #699E97 68.77%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
.container form{
  padding: 30px 0 0 0;
}
.container form .form-row{
  display: flex;
  margin: 32px 0;
}
form .form-row .input-data{
  width: 100%;
  height: 40px;
  margin: 0 20px;
  position: relative;
}
form .form-row .textarea{
  height: 70px;
}
.input-data input,
.textarea textarea{
  display: block;
  width: 100%;
  height: 100%;
  border: none;
  font-size: 17px;
  border-bottom: 2px solid rgba(0,0,0, 0.12);
}
.input-data input:focus ~ label, .textarea textarea:focus ~ label,
.input-data input:valid ~ label, .textarea textarea:valid ~ label{
  transform: translateY(-30px);
  font-size: 14px;
  color: #3498db;
}
.textarea textarea{
  resize: none;
  padding-top: 10px;
}
.input-data label{
  position: absolute;
  pointer-events: none;
  bottom: 10px;
  font-size: 16px;
  transition: all 0.3s ease;
}
.textarea label{
  width: 100%;
  bottom: 40px;
  background: #fff;
}
.input-data .underline{
  position: absolute;
  bottom: 0;
  height: 2px;
  width: 100%;
}
.input-data .underline:before{
  position: absolute;
  content: "";
  height: 2px;
  width: 100%;
  background: #3498db;
  transform: scaleX(0);
  transform-origin: center;
  transition: transform 0.3s ease;
}
.input-data input:focus ~ .underline:before,
.input-data input:valid ~ .underline:before,
.textarea textarea:focus ~ .underline:before,
.textarea textarea:valid ~ .underline:before{
  transform: scale(1);
}
.submit-btn .input-data{
  overflow: hidden;
  height: 45px!important;
  width: 25%!important;
}
.submit-btn .input-data .inner{
  height: 100%;
  width: 300%;
  position: absolute;
  left: -100%;
  background: -webkit-linear-gradient(112.07deg, #79B4AE 33.17%, #699E97 68.77%);
  transition: all 0.4s;
}
.submit-btn .input-data:hover .inner{
  left: 0;
}
.submit-btn .input-data input{
  background: none;
  border: none;
  color: #fff;
  font-size: 17px;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 1px;
  cursor: pointer;
  position: relative;
  z-index: 2;
}

.submit-btn .input-data select{
    background: none;
  border: none;
  color: #000;
  font-size: 17px;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 1px;
  cursor: pointer;
  position: relative;
  z-index: 2;
}
</style>
