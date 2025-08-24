import {  useQuery } from "react-query";
import authAxios from "../../../Axios/authAxios";
// eslint-disable-next-line @typescript-eslint/no-explicit-any
export const useGetUsers=()=>{
    const getUsers=async ()=>{
        try{
            const res=await authAxios.get("api/v1/user/details",{
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
        queryKey:["getUsers"],
        queryFn:getUsers,
    });
    return{
        isLoading,
        error,
        data,
        refetch,
    };
};