
import * as yup from "yup";
export const schema= yup.object({
    task:yup
    .string()
    .min(3)
    .required(),

    status:yup.string(),
    // .required(),

     priority:yup.string(),
    // .required(),
    
    assignee:yup.object()
    .required(),
        
    due_date:yup.date()
    .required(),

    // project_id:yup.number()
    // .required(),
})