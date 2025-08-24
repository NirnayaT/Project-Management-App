import { useMutation } from "react-query";

import noAuthAxios from "../../../Axios/noAuthAxios";
type DeleteProjectParams={
	project_id:number;
	owner_id:number;
}
// eslint-disable-next-line @typescript-eslint/no-explicit-any
type OnSuccessCallback = (data: any) => void;
export const useDeleteProj = (onSuccess:OnSuccessCallback) => {
	// eslint-disable-next-line @typescript-eslint/no-unused-vars
	const deleteProj = async({ project_id, owner_id }: DeleteProjectParams) => {
		try {
			const res = await noAuthAxios.delete("api/v1/projects/remove", {
				data: { project_id,owner_id },
			});
			console.log("data after deletion =>", res);
			if (res) {
				console.log("Deleted successfully", project_id);
			}
		} catch (error) {
			console.error(error);
		}
	};

	const mutation = useMutation(deleteProj, {
		onSuccess,
	});

	return {
		mutation,
	};
};
