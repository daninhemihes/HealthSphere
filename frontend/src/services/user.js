import axios from 'axios'
const API_URL = `http://127.0.0.1:8000/api`;

class UserService {
    async login(username, password) {
        try{
            const response = await axios.post(`${API_URL}/login/`, {
                username: username,
                password: password,
            });
            return response
        } catch (error) {
            console.error('Error while logging in: ', error);
            return
        }
    }
    async register(username, email, password){
        try{
            const response = await axios.post(`${API_URL}/register/`, {
                username: username,
                email: email,
                password: password
            });
            return response
        } catch (error) {
            console.error('Error while registering user: ', error);
            return
        }
    }

}

export default new UserService()