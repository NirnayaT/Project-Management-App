// import React from "react";

// import { Input, InputNumber } from "antd";
// import { Controller, Control } from 'react-hook-form';
// import { SizeType } from "antd/es/config-provider/SizeContext";

// interface InputNumberProps{
//     errors?: string;
   
    
//     width?:string |number;
//     // eslint-disable-next-line @typescript-eslint/no-explicit-any
//     control: Control<any>;
//     name: string;
//     className?:string;
//     defaultValue?:number
//     disabled?:boolean
//      min?:number
//      max?:number
// }
// const InputNumberField:React.FC<InputNumberProps> = (
//     {
//         // field,
//         control,
//         errors,
//         size = 'default',
//         placeholder = 'Enter', 
//         prefix,
        
//         name,
//         className,
//         defaultValue,
//         disabled,
//           min,max
//     }
// )=>(<div className="email w-[100%]">
//   {!control&&(
//     <InputNumber
//       // {...field}
//       control={control}
//       size={size}
//       placeholder={placeholder}
      
//       prefix={prefix}
//       className={className}
//       defaultValue={defaultValue}
//       disabled={disabled}
//       min={min}
//       max={max}
//     />
//   )}
//   {control&&(
//     <Controller
//       // {...field}
//       name={name}
//       control={control}
//       render={({field})=>{
//         return(
//           <InputNumber
//           {...field}
//           size={size}
//           placeholder={placeholder}
//           prefix={prefix}
//           className={className}
//           defaultValue={defaultValue}
//           disabled={disabled}
//           min={min}
//           max={max}
//           />
//         )
//       }}
//     />
//   )}

//     {errors && <p className="text-[red]">{errors}</p>}
//   </div>

// );
// export default InputNumberField;