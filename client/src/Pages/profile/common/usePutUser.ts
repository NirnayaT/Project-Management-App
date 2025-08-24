import { useMutation } from "react-query";


import authAxios from "../../../Axios/authAxios";

// eslint-disable-next-line @typescript-eslint/no-explicit-any
export const usePutUser = (onSuccess:any) => {
	const updateUserFn = async ({ id:number, data:any }) => {
		try {
			const res = await authAxios.put(`/update/${id}`, data);
			console.log("response from update", res);
			if (res) {
				console.log("res>>>", res);
				console.log("Successfully Updated");
			}
		} catch (error) {
			console.log("Error while updating data", error);
		}
	};
	const mutation = useMutation(updateUserFn, {
		onSuccess,
	});
	return {
		mutation,
	};
};
