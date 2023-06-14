import axios from 'axios'
const API_URL = `http://127.0.0.1:8000/api`;

class ProfileTabService {
    async getInfo(username) {
        try{
            const response = await axios.get(`${API_URL}/info_person/${username}/`, {
                username: username
            });
            return response
        } catch (error) {
            console.error('Error while getting profile info: ', error);
            return
        }
    }
    async setInfo(user, data){
        try{
            const response = await axios.post(`${API_URL}/info_person/`, {
                username: data.username,
                firstName : data.firstName,
                lastName : data.lastName,
                sex: data.sex,
                birthDate: data.birthDate,
                bloodType: data.bloodType,
                organDonor: data.organDonor,
                weight: data.weight,
                height: data.height,
                maritalStatus : data.maritalStatus,
                color : data.color,
                nationality : data.nationality,
                occupation : data.occupation,
                address : data.address,
                phone : data.phone,
                primaryLanguague: data.primaryLanguague
            });
            return response
        } catch (error) {
            console.error('Error while setting profile info: ', error);
            return
        }
    }
    async updateInfo(user, data){
        try{
            console.log(data)
            const response = await axios.put(`${API_URL}/info_person/${user}/`, {
                username: data.username,
                firstName : data.firstName,
                lastName : data.lastName,
                sex: data.sex,
                birthDate: data.birthDate,
                bloodType: data.bloodType,
                organDonor: data.organDonor,
                weight: data.weight,
                height: data.height,
                maritalStatus : data.maritalStatus,
                color : data.color,
                nationality : data.nationality,
                occupation : data.occupation,
                address : data.address,
                phone : data.phone,
                primaryLanguague: data.primaryLanguague
            });
            return response
        } catch (error) {
            console.error('Error while setting profile info: ', error);
            return
        }
    }
    async getEmergencyContact(username) {
        try{
            const response = await axios.get(`${API_URL}/contato_emergencia/${username}/`, {
                username: username
            });
            console.log(response)
            return response
        } catch (error) {
            console.error('Error while getting emergency contact: ', error);
            return
        }
    }
    async setEmergencyContact(user, data){
        try{
            const response = await axios.post(`${API_URL}/contato_emergencia/`, {
                username: data.username,
                name: data.name,
                relationship: data.relationship,
                phone: data.phone
            });
            return response
        } catch (error) {
            console.error('Error while setting emergency contact: ', error);
            return
        }
    }
}

export default new ProfileTabService()