import axios from "axios";
import { BASE_URL } from "../Constant/constant";
const access_token = localStorage.getItem("access_token")
const axiosNoAuth = axios.create({
  baseURL: BASE_URL,
  // timeout: 3000,
});

axiosNoAuth.interceptors.request.use(function (config) {
  config.headers['ngrok-skip-browser-warning'] = 'false';
  config.headers['Authorization'] = `Bearer ${access_token}`;
  // Do something before request is sent
  return config;
}, function (error) {
  // Do something with request error
  return Promise.reject(error);
});
export default axiosNoAuth;