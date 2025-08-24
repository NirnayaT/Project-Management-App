import {  useQuery } from "react-query";
import authAxios from "../../../Axios/authAxios";
// import { AuthHook } from "../../Auth/Hook/useLoginHook";
export const useGetUser=()=>{
    const getUser=async ()=>{
        try{
            const res=await authAxios.get(`api/v1/user`,{
                headers:{
                    Accept:"application/json",
                },
            });
            console.log("res.data from useGetUsers==>", res.data);
			return res.data;
        }
        catch(error){
            console.log("Error while fetching data:",error)
        }
    };
    const{isLoading,error,data,refetch}=useQuery({
        queryKey:["getUser"],
        queryFn:getUser,
    });
    return{
        isLoading,
        error,
        data,
        refetch,
    };
};