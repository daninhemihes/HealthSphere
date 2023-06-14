<template>
    <div class="container">
        <div class="text">
            Seus Contatos
        </div>
        <form action="#">
            <div class="form-row">
                    <div class="input-data">
                        <input type="text" v-model="newEmergencyContact.name" required>
                        <div class="underline"></div>
                        <label for="">Nome</label>
                    </div>
                    <div class="input-data">
                        <input type="text" v-model="newEmergencyContact.relationship" required>
                        <div class="underline"></div>
                        <label for="">Relacionamento</label>
                    </div>
                    <div class="input-data">
                        <input type="number" v-model="newEmergencyContact.phone" required>
                        <div class="underline"></div>
                        <label for="">Telefone</label>
                    </div>
                    <div class="input-data">
                        <div class="inner"></div>
                        <input type="submit" value="Salvar" @click="saveContact()">
                    </div>
            </div>
        </form>
        <div class="seus-contatos">
            <table>
                <thead>
                    <tr>
                        <th>Nome</th>
                        <th>Relaçao</th>
                        <th>Telefone</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(contact, index) in emergencyContacts" :key="index">
                        <td>{{ contact.name }}</td>
                        <td>{{ contact.relationship }}</td>
                        <td>{{ contact.phone }}</td>
                    </tr>
                </tbody>
            </table>
        </div>
      </div>
</template>

<script>  
import ProfileService from '../services/profile'

export default {
    name: 'Contacts',
    components: {
    
},
data(){
    return{
        newEmergencyContact:{
            username: localStorage.getItem("username"),
            name: '',
            relationship: '',
            phone: ''
        },
        emergencyContacts: []
    }
},
async mounted() {
    await this.getContacts()
},
methods:{
    async getContacts(){
        try{
            const emergencyContacts = await ProfileService.getEmergencyContact(localStorage.getItem("username"))
            this.emergencyContacts = emergencyContacts.data
            console.log(this.emergencyContacts)
        } catch (error) {
            console.log("There was an error while getting contacts: " + error)
        }
    },
    async saveContact(){
        try{
            await ProfileService.setEmergencyContact(localStorage.getItem("username"), this.newEmergencyContact)
            alert('Contato salvo!')
            this.getContacts()
        } catch (error) {
            console.log("There was an error while getting contacts: " + error)
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
table {
    border-collapse: collapse;
    width: 100%;
    color: #333;
    font-family: Arial, sans-serif;
    font-size: 14px;
    text-align: left;
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
    margin: auto;
    margin-top: 50px;
    margin-bottom: 50px;
  }
  table th {
  background-color: #236067;
  color: #fff;
  font-weight: bold;
  padding: 10px;
  text-transform: uppercase;
  letter-spacing: 1px;
  border-top: 1px solid #fff;
  border-bottom: 1px solid #ccc;
}
table tr:nth-child(even) td {
  background-color: #f2f2f2;
}

table tr:hover td {
  background-color: #B0DCDB;
}
table td {
  background-color: #fff;
  padding: 10px;
  border-bottom: 1px solid #ccc;
  font-weight: bold;
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
  transform: translateY(-20px);
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
  background: -webkit-linear-gradient(right, #56d8e4, #9f01ea, #56d8e4, #9f01ea);
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

</style>
