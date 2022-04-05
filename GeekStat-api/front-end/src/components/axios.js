import axios from 'axios'

const instance = axios.create({
    headers : {
        'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8'
    },
    withCredentials:false,
    baseURL: 'https://geekstat-api.herokuapp.com/'
});

export default instance;