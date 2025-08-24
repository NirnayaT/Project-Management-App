import {  useForm } from "react-hook-form";
import { yupResolver } from "@hookform/resolvers/yup";
import { MailOutlined, LockFilled } from "@ant-design/icons";
import { Checkbox, Button, Card } from "antd";
import {useNavigate} from "react-router-dom";
import type { CheckboxProps } from "antd";
import axios from "axios";

import InputField from "../../Components/Atoms/Input/InputField";
import PasswordInput from "../../Components/Atoms/Input/PasswordInput";
import { schema } from "./LoginSchema";
import "../../Theme/Css/Login.css";

import { AuthHook } from "./Hook/useLoginHook";
type formValues = {
	username: string;
	password: string;
};

export default function Login() {
	const {setOwnerId}=AuthHook();
	const navigate= useNavigate();
	const onChange: CheckboxProps["onChange"] = (e) => {
		console.log(`checked = ${e.target.checked}`);
	};
	const {
		control,
		handleSubmit,
		// watch,
		formState: { errors },
	} = useForm<formValues>({
		defaultValues: {
			username: "",
			password: "",
		},
		resolver: yupResolver(schema),
	});
	// const onSuccess =()=>{
	// 	console.log("doneeeeee")
	// }
	// const {mutation}=usePostLogin(onSuccess);
	const onSubmit = async (data: formValues) => {
		try{
			console.log("done", data); 
			console.log("submitted");
			// mutation.mutate(data);


			const {username,password}=data

			const payload=new URLSearchParams({username:username, password:password})
			console.log("payload==>",payload)

			const res = await axios.post(
				"http://127.0.0.1:8000/api/v1/user/login",
				payload
			);
			console.log("response==>", res);
			if (res) {
				localStorage.setItem("access_token", res?.data?.access_token);
				localStorage.setItem("refresh_token",res?.data?.refresh_token);
				console.log("the token ==>", res.data.access_token);

				setOwnerId(res.data.owner_id);
				navigate("/home");
			}

		}catch(error){
			console.log(error);
			// notifyLoginFailed("login failed");

		}
	};
	const onError=()=>{
		console.log("error occured")

	};
	const handleCreate=()=>{
		navigate("/register")
	}
	// useEffect(() => {
	// 	const subscription = watch((value, { name, type }) =>
	// 		console.log(value, name, type)
	// 	);
	// 	return () => subscription.unsubscribe();
	// }, [watch]);
	// const username = watch('username', '')
	// console.log(username)
	return (
		<>
			<Card
				style={{
					width: 390,
					backgroundColor: "white",
					margin: "100px auto 0",
					boxShadow: "0 0 10px rgba(0, 0, 0, 0.1)",
				}}
				
			>
				<div
					style={{ fontFamily: "'Anton', sans-serif" }}
					className="flex justify-center relative bottom-14 p-5 rounded-md text-white text-xl bg-[#172b4d]"
				>
					Sign In
				</div>

				<form onSubmit={handleSubmit(onSubmit,onError)} className="flex flex-col">
					<div className="username mb-4">
						{/* <Controller
							control={control}
							name="ReactDatepicker"
							{...register("email")}
							render={({ field }) => ( */}
								<InputField
									errors={errors.username?.message}
									size="large"
									type="email"
									placeholder="Enter your username"
									prefix={<MailOutlined />}
									control={control}
									name={'username'}
								/>
							{/* )} */}
						{/* /> */}
					</div>
					<div className="password mb-4">
						{/* <Controller
							control={control}
							{...register("password")}
							render={({ field }) => ( */}
								<PasswordInput
									errors={errors.password?.message}
									size="large"
									placeholder="Enter your password"
									prefix={<LockFilled />}
									control={control}
									name={'password'}
								/>
							{/* )}
						/> */}
					</div>
					<Checkbox onChange={onChange} className="mb-4">
						Remember me
					</Checkbox>
					<Button
						style={{ backgroundColor: "#172b4d", color: "white" }}
						htmlType="submit"
					>
					Login
					</Button>					
				</form>
				<div className=" flex justify-between mt-12">
					<div>Forgot password?</div>
					<div onClick={()=>{handleCreate()}} style={{cursor:"pointer"}}>Create new account</div>
				</div>
			</Card>
		</>
	);
}