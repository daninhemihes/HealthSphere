import axios from 'axios'
const API_URL = `http://127.0.0.1:8000/api`;

class MedicalService {
    async getConditions(username) {
        try{
            const response = await axios.get(`${API_URL}/condicoes_medical/${username}/`, {
                username: username
            });
            console.log(response)
            return response
        } catch (error) {
            console.error('Error while getting medical condition: ', error);
            return
        }
    }
    async getAllergies(username) {
        try{
            const response = await axios.get(`${API_URL}/reacoes_alergicas/${username}/`, {
                username: username
            });
            console.log(response)
            return response
        } catch (error) {
            console.error('Error while getting medical condition: ', error);
            return
        }
    }
    async setCondition(user, data){
        try{
            const response = await axios.post(`${API_URL}/condicoes_medical/`, {
                username: data.username,
                medicalCondition : data.medicalCondition,
                note : data.note
            });
            return response
        } catch (error) {
            console.error('Error while setting medical condition: ', error);
            return
        }
    }
    async setAllergie(user, data){
        try{
            const response = await axios.post(`${API_URL}/reacoes_alergicas/`, {
                username: data.username,
                allergiesReactions : data.allergiesReactions,
                notes : data.notes
            });
            return response
        } catch (error) {
            console.error('Error while setting medical condition: ', error);
            return
        }
    }
}

export default new MedicalService()