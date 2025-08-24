import axios from "axios";
import { BASE_URL } from '../Constant/constant'

const access_token = localStorage.getItem("access_token")
console.log("access_token>>>", access_token)

const authAxios = axios.create({
  baseURL: BASE_URL,
  // timeout: 1000,
});

authAxios.interceptors.request.use(function (config) {
  config.headers['Authorization'] = `Bearer ${access_token}`;
  config.headers['ngrok-skip-browser-warning'] = 'false';
  // Do something before request is sent
  return config;
}, function (error) {
  // Do something with request error
  return Promise.reject(error);
});

// Add a response interceptor
authAxios.interceptors.response.use(function (response) {
  console.log("response>>>", response)
  // Any status code that lie within the range of 2xx cause this function to trigger
  // Do something with response data
  if (response.headers['content-type'] !== 'application/json') {
    throw new Error('Non-JSON response');
  }

  return response;
}, function (error) {
  // Any status codes that falls outside the range of 2xx cause this function to trigger
  // Do something with response error
  return Promise.reject(error);
});

export default authAxios;