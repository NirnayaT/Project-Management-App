import { useMutation } from "react-query";

import noAuthAxios from "../../../Axios/noAuthAxios";
type DeleteTaskParams={
	project_id:number;
	task_id:number;
}
// eslint-disable-next-line @typescript-eslint/no-explicit-any
type OnSuccessCallback = (data: any) => void;
export const useDelTask = (onSuccess:OnSuccessCallback) => {
	// eslint-disable-next-line @typescript-eslint/no-unused-vars
	const delTask = async({task_id, project_id,  }: DeleteTaskParams) => {
		try {
			const res = await noAuthAxios.delete("api/v1/tasks/remove", {
				data: {task_id, project_id },
			});
			console.log("data after deletion =>", res);
			if (res) {
				console.log("Deleted successfully", task_id);
			}
		} catch (error) {
			console.error(error);
		}
	};

	const mutation = useMutation(delTask, {
		onSuccess,
	});

	return {
		mutation,
	};
};
