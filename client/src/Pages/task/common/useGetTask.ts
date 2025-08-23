import {  useQuery } from "react-query";
import authAxios from "../../../Axios/authAxios";
// eslint-disable-next-line @typescript-eslint/no-explicit-any
export const useGetTaskUser=()=>{
    const getTaskUser=async ()=>{
        try{
            const res=await authAxios.get(`api/v1/tasks/show/user`,{
                headers:{
                    Accept:"application/json",
                },
            });
            console.log("res.data from useGetTask==>", res.data);
			return res.data;
        }
        catch(error){
            console.log("Error while fetching data:",error)
        }
    };
    const{isLoading,error,data,refetch}=useQuery({
        queryKey:["getTaskUser"],
        queryFn:getTaskUser,
    });
    return{
        isLoading,
        error,
        data,
        refetch,
    };
};
export const useGetTask=(id:number)=>{
    const getTask=async ()=>{
        try{
            const res=await authAxios.get(`api/v1/tasks/show?project_id=${id}`,{
                headers:{
                    Accept:"application/json",
                },
            });
            console.log("res.data from useGetTask==>", res.data);
			return res.data;
        }
        catch(error){
            console.log("Error while fetching data:",error)
        }
    };
    const{isLoading,error,data,refetch}=useQuery({
        queryKey:["getTask"],
        queryFn:getTask,
    });
    return{
        isLoading,
        error,
        data,
        refetch,
    };
};