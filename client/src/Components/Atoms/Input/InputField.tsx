import React from "react";

import { Input } from "antd";
import { Controller, Control } from 'react-hook-form';
import { SizeType } from "antd/es/config-provider/SizeContext";

interface InputProps{
    errors?: string;
    size?:SizeType;
    placeholder?: string; 
    prefix?: React.ReactNode;
    type:string;
    width?:string |number;
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    control: Control<any>;
    name: string;
    className?:string;
    defaultValue?:string
    disabled?:boolean
}
const InputField:React.FC<InputProps> = (
    {
        field,
        control,
        errors,
        size = 'default',
        placeholder = 'Enter', 
        prefix,
        type="text",
        name,
        className,
        defaultValue,
        disabled
    }
)=>(<div className="email w-[100%]">
  {!control&&(
    <Input
      {...field}
      control={control}
      size={size}
      placeholder={placeholder}
      type={type}
      prefix={prefix}
      className={className}
      defaultValue={defaultValue}
      disabled={disabled}
    />
  )}
  {control&&(
    <Controller
      {...field}
      name={name}
      control={control}
      render={({field})=>{
        return(
          <Input
          {...field}
          size={size}
          placeholder={placeholder}
          type={type}
          prefix={prefix}
          className={className}
          defaultValue={defaultValue}
          disabled={disabled}
          />
        )
      }}
    />
  )}

    {errors && <p className="text-[red]">{errors}</p>}
  </div>

);
export default InputField;