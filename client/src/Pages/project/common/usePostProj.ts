import { useMutation } from "react-query";
import authAxios from "../../../Axios/authAxios";

// eslint-disable-next-line @typescript-eslint/no-explicit-any
export const usePostProj = (onSuccess: any) => {
	
	// eslint-disable-next-line @typescript-eslint/no-explicit-any
	const postProj = async (data: any) => {
		console.log("data after creatindfjdshg", data);
		try {
			// const res = await axiosNoAuth.post("/user", data);
			const res = await authAxios.post("api/v1/projects/create", data);
			return res.data;
		} catch (error) {
			console.log("Error fetching data:", error);
		}
	};
	const mutation = useMutation(postProj, {
		onSuccess,
	});
	return {
		mutation,
	};
};
