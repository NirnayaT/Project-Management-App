
import * as yup from "yup";
export const schema= yup.object({
    project_name:yup
    .string()
    .min(3)
    .required("project name is required"),

    project_description:yup.string()
    .required("Description is required")
    .min(10),

    start_date:yup.date()
    .required("Start date is required"),
    
    end_date:yup.date()
    .required("Ends date is required"),
        
    owner_id:yup.number()
    .required("required"),

})