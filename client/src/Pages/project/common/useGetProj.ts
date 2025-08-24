import {  useQuery } from "react-query";
import authAxios from "../../../Axios/authAxios";
import { AuthHook } from "../../Auth/Hook/useLoginHook";
export const useGetProj=()=>{
    const {ownerId}=AuthHook();
    console.log("value of owner id",ownerId)
    const getProj=async ()=>{
        try{
            const res=await authAxios.get(`api/v1/projects/show`,{
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
        queryKey:["getProj"],
        queryFn:getProj,
    });
    return{
        isLoading,
        error,
        data,
        refetch,
    };
};