
import * as yup from "yup";
export const schema= yup.object({
    username:yup
    .string()
    .email("invalid email")
    .required("email is required"),

    
    password:yup.string()
    .required("password is required")
    .min(8)
    
})