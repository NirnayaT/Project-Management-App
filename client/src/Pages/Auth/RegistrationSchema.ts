
import * as yup from "yup";
export const schema= yup.object({
    email:yup
    .string()
    .email("invalid email")
    .required("email is required"),
    
    password:yup.string()
    .required("password is required")
    .min(8),
    
    username:yup.string()
    .required("username is required")
    .min(3),
    
})