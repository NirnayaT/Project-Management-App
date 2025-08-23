import React from 'react';
import moment from 'moment';

import { DatePicker } from 'antd';
import { Controller, Control } from 'react-hook-form';

interface DateProps {
  errors?: string;
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  control: Control<any>; // Type Control<any> is correct
  name: string;
  
}
const handleChange = (date: moment.Moment | null, onChange: (value: Date | null) => void) => {

  onChange(date ? date.toDate() : null); // Convert moment to native Date and call onChange
  console.log('date>>>', date?.format("YYYY-MM-DD"))
};

const Dates: React.FC<DateProps> = ({
  control,
  errors,
  name,
}) => (
  <div className=' w-[100%]'>
    <Controller
      name={name}
      control={control}
      render={({ field }) => {
        return (
          <DatePicker
            {...field}
          
            value={field.value ? moment(field.value) : null}
            onChange={(date) => handleChange(date, field.onChange)}
          />
        )
      }}
    />
    {errors && <p className="text-[red]">{errors}</p>}
  </div>
);

export default Dates;