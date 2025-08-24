import { useMutation } from 'react-query';

import authAxios from '../../../Axios/authAxios';

export const useUpdateTask = (onSuccess: () => void) => {
    const mutation = useMutation(
      (data: any) => {
        console.log("Sending update request with data:", data);
        return authAxios.put(`/api/v1/tasks/update`, data);
      },
      {
        onSuccess: () => {
          console.log("Update successful");
          onSuccess();
        },
      }
    );
  
    return { mutation };
  };
  
