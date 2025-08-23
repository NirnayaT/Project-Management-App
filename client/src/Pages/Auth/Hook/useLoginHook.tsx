import { createContext, useContext, useState } from "react";
type loginValue={
     // eslint-disable-next-line @typescript-eslint/no-explicit-any
     ownerId:any;
     // eslint-disable-next-line @typescript-eslint/no-explicit-any
     setOwnerId:React.Dispatch<React.SetStateAction<any>>;
}
const Authcontext=createContext<loginValue>({
     ownerId:undefined,
     setOwnerId:()=>void{},
});
interface authProviderProps{
     children:React.ReactNode;
}
export const AuthProvider:React.FC<authProviderProps>=({children})=>{
     // eslint-disable-next-line @typescript-eslint/no-explicit-any
     const [ownerId,setOwnerId]=useState<any>(null)
     return(
          <Authcontext.Provider value={{ownerId,setOwnerId}}>
               {children}
          </Authcontext.Provider>
     )
}
export const AuthHook=()=>{
     return useContext(Authcontext);
};
