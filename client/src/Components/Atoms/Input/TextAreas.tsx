import React from 'react';

import { Input } from 'antd';
import { Controller, Control } from 'react-hook-form';

const { TextArea } = Input;

interface TextProps {
  errors?: string;
  placeholder?: string;
  row?: number;
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  control: Control<any>; // Type Control<any> is correct
  name: string;
}

const TextAreas: React.FC<TextProps> = ({
  control,
  errors,
  placeholder = 'Enter',
  row = 4,
  name
}) => (
  <div className="email w-[100%]">
    <Controller
      name={name}
      control={control}
      render={({ field }) => (
        <TextArea
          {...field}
          rows={row}
          placeholder={placeholder}
          className="ps-2 w-[100%] mt-4"
        />
      )}
    />
    {errors && <p className="text-[red]">{errors}</p>}
  </div>
);

export default TextAreas;
