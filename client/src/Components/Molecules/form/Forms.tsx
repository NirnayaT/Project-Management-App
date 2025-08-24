// import { useForm } from 'react-hook-form';
// import { yupResolver } from '@hookform/resolvers/yup';
// import { schema } from '../../../Pages/project/ProjectSchema';

// import InputField from '../../Atoms/Input/InputField';
// import TextAreas from '../../Atoms/Input/TextAreas';
// import Dates from '../../Atoms/Input/Dates';
// import { usePostProj } from '../../../Pages/project/common/usePostProj';

// type projectForm={
//   projName:string;
//   projDesc:string;
//   startDate:Date |null;
//   endDate:Date |null;
// } 

// const Forms = () => {
//   //Destructuring
//   const {
//     control,
//     handleSubmit,
//     formState: {  isValid },
//   } = useForm<projectForm>({
//     defaultValues:{
//       projName:"",
//       projDesc:"",
//       startDate:null,
//       endDate:null
//     },
//     resolver:yupResolver(schema),
//   });
//   const onSuccess = () => {
//     console.log("created successfully");
//   };
//   const { mutation } = usePostProj(onSuccess);

//   const onSubmit = async (data:projectForm) => {
//     // mutate trigger the mutation operation defined in your useMutation setup.
//     mutation.mutate(data);
//   };
//   const onError = (errors:string) => {
//     console.log("form Errors==>", errors);
//   };
//     <form
//     className=" flex-col w-96  mt-20 p-10 bg-white"
//     onSubmit={handleSubmit(onSubmit, onError)}
//   >
//     {/* project name */}
//     <div className="flex flex-col bg-white">
//       <div className="flex justify-between bg-white">
//         <label className="bg-white">project Name:</label>
//         <InputField
//             errors='errors.title?.message'
//             control={control}
//             name={"projName"}
//             size='large'
//             type={'text'}/>

//       </div>
//     </div>
//     <br />a
//     <br />

//     {/* project description */}
//     <div className="flex flex-col  bg-white">
//       <div className="flex justify-between bg-white">
//         <label className="bg-white">Description</label>
//         <TextAreas/>
//       </div>
//     </div>
//     <br />
//     <br />
    

//     <div className="flex flex-col justify-between bg-white ">
//       <div className="flex justify-between bg-white">
//         <label className="bg-white">Start Date:</label>
//          <Dates/>
//       </div>

    
//     </div>
//     <div className="flex flex-col justify-between bg-white ">
//       <div className="flex justify-between bg-white">
//         <label className="bg-white">End Date:</label>
//          <Dates/>
//       </div>
//     </div>

//     {/* submit button */}
//     <div className="bg-white mt-10  flex justify-center">
//       <button
//         type="submit"
//         className="bg-sky-200 px-5 py-2 rounded "
//         disabled={!isValid}
//       >
//         SUBMIT
//       </button>
//     </div>
//   </form>

// }

// export default Forms
