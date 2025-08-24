import { useForm } from 'react-hook-form';
import { yupResolver } from '@hookform/resolvers/yup';
import { schema } from './ProjectSchema';
import { Button } from 'antd';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import {faCalendar} from '@fortawesome/free-solid-svg-icons';
import type { InputNumberProps } from 'antd';
import { useNavigate } from 'react-router-dom';

import InputField from '../../Components/Atoms/Input/InputField';
import { usePostProj } from './common/usePostProj';
import moment from 'moment';
import TextAreas from '../../Components/Atoms/Input/TextAreas';
import Dates from '../../Components/Atoms/Input/Dates';
import '../../Theme/Css/Project.css'
type ProjectForm = {
  project_name: string;
  project_description: string;
  start_date: Date | null; 
  end_date: Date | null;  
  owner_id:number; 
};

const Project = () => {
  const navigate=useNavigate();
  const { control, handleSubmit } = useForm<ProjectForm>({
    defaultValues: {
      project_name:"",
      project_description:"",
      start_date:null,
      end_date:null,
      owner_id:1,
    },
    resolver: yupResolver(schema),
  });

  const onSuccess = () => {
    // console.log('project created successfully');
    navigate('/project')
  };

  const { mutation } = usePostProj(onSuccess);

  const onSubmit = async (data: ProjectForm) => {
    console.log("on the way of submitings")
    const formattedStartDate = moment(data.start_date).format('YYYY-MM-DD');
    const formattedEndDate = moment(data.end_date).format('YYYY-MM-DD');

    const formattedData = {
      ...data,
      start_date: formattedStartDate, 
      end_date: formattedEndDate
    };
    mutation.mutate(formattedData);
  };
  // const onChange: InputNumberProps['onChange'] = (value) => {
  //   console.log('changed', value);
  // };
  const handleCancel=()=>{
    navigate('/project')
  }
  return (
    <div className='flex justify-center relative'>
      <div className='absolute top-[25px] left-[80px] flex w-[65px] h-[65px] justify-center items-center rounded bg-zinc-300	'>
        <FontAwesomeIcon icon={faCalendar} className='w-[25px] h-[25px] '/>
      </div>
    <form
      className="flex-col w-full mt-10 p-10 ps-[70px] justify-center bg-white shadow-xl rounded"
      onSubmit={handleSubmit(onSubmit)}
    >
      <div className="text-2xl font-bold text-center mb-5 absolute top-[65px] left-[165px]">New Project</div>
      <div className="flex flex-col ">
        <div className=" input-field-div items-center justify-between p-[0.5rem] mt-[65px] relative">
          <label className="inline project-label w-[8rem]">Project Name:</label>
          <InputField
            control={control}
            name="project_name"
            type="text"
            size="large" 
            className="mt-5 inputFields border-0 border-b-2   rounded-none focus:placeholder-transparent "           
          />
        </div>
      </div>
      <br />
      <br />
      <div className="flex flex-col ">
        <div className="items-center justify-between  p-[0.5rem] ">
          <label className="inline w-[8rem] ">Project Description:</label>
          <TextAreas
            control={control}
            name="project_description"
            row={3}
          />
        </div>
      </div>
      <br />
      <br />
      
      <div className="flex flex-col ">
        <div className="flex items-center justify-between w-[30rem] p-[0.5rem] ">
          <label className="inline w-[8rem]">Start Date:</label>
          <Dates
            control={control}
            name="start_date"
          />
        </div>
      </div>
      <br />
      <br />
      <div className="flex flex-col ">
        <div className="flex items-center justify-between w-[30rem] p-[0.5rem]">
          <label className="inline w-[8rem]">End Date:</label>
          <Dates
            control={control}
            name="end_date"
          />
        </div>
      </div>
      <br />
      <br />
      <div className='flex justify-end'>
        <Button onClick={handleCancel} className='px-9 font-medium me-7'>Cancel</Button>
        <Button  htmlType='submit' type='primary' className='px-9 font-medium' >Create</Button>
      </div>

    </form>
    </div>
  );
};

export default Project;
