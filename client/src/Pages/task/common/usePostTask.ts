import { useMutation } from "react-query";
import authAxios from "../../../Axios/authAxios";
// import axiosNoAuth from "../../axios/axios";

// eslint-disable-next-line @typescript-eslint/no-explicit-any
export const usePostTask = (onSuccess: any) => {
	console.log("use post taskkkkk")
	// eslint-disable-next-line @typescript-eslint/no-explicit-any
	const postTask = async (data: any) => {
		console.log("Task after creatingfkjhfdkjghg", data);
		try {
			// const res = await axiosNoAuth.post("/user", data);
			const res = await authAxios.post("api/v1/tasks/add", data);
			return res.data;
		} catch (error) {
			console.log("Error fetching data:", error);
		}
	};
	const mutation = useMutation(postTask, {
		onSuccess,
	});
	return {
		mutation,
	};
};
