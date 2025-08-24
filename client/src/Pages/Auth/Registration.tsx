import { useForm } from "react-hook-form";
import { yupResolver } from "@hookform/resolvers/yup";
import { MailOutlined, LockFilled,UserOutlined } from "@ant-design/icons";
import { Checkbox, Button, Card } from "antd";
import type { CheckboxProps } from "antd";
import axios from "axios";

import InputField from "../../Components/Atoms/Input/InputField";
import PasswordInput from "../../Components/Atoms/Input/PasswordInput";
import { schema } from "./RegistrationSchema";
import "../../Theme/Css/Login.css";

import { useEffect } from "react";
import { useNavigate } from "react-router-dom";

type formValues = {
	username: string;
	email: string;
	password: string;
};
export default function Registration() {
	const navigate=useNavigate();
	const onChange: CheckboxProps["onChange"] = (e) => {
		console.log(`checked = ${e.target.checked}`);
	};
	const {
		control,
		handleSubmit,
		watch,
		formState: { errors },
	} = useForm<formValues>({
		defaultValues: {
			email: "",
			password: "",
			username:"",
		},
		resolver: yupResolver(schema),
	});
	const onSubmit = async (data: formValues) => {
		try{
			console.log("done", data); 
			console.log("submitted");
			// mutation.mutate(data);

			const res = await axios.post(
				"http://127.0.0.1:8000/api/v1/user/register",
				data
			);
			console.log("response==>", res);
			if (res) {
				localStorage.setItem("access_token", res?.data?.access_token);
				// localStorage.setItem("refresh_token",res?.data?.refresh_token);
				console.log("the token ==>", res.data.access_token);
				navigate("/");
			}

		}catch(error){
			console.log(error);
			// notifyLoginFailed("login failed");

		}
	};
	useEffect(() => {
		const subscription = watch((value, { name, type }) =>
			console.log(value, name, type)
		);
		return () => subscription.unsubscribe();
	}, [watch]);
	const handleSignIn=()=>{
		navigate("/");
	}

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
					REGISTRATION
				</div>

				<form onSubmit={handleSubmit(onSubmit)} className="flex flex-col">
					<div className="username mb-4">
								<InputField
									errors={errors.username?.message}
									size="large"
									type="text"
									placeholder="Enter your Username"
									prefix={<UserOutlined />}
									name={'username'}
									control={control}
								/>
					</div>
					<div className="email mb-4">
								<InputField
									// field={field}
									errors={errors.email?.message}
									size="large"
									type="email"
									placeholder="Enter your email"
									prefix={<MailOutlined />}
									control={control}
									name={'email'}
								/>
					</div>
					<div className="password mb-4">
								<PasswordInput
									// field={field}
									errors={errors.password?.message}
									size="large"
									placeholder="Enter your password"
									prefix={<LockFilled />}
									control={control}
									name={'password'}
								/>
					</div>
					<Checkbox onChange={onChange} className="mb-4">
					I agree the Terms and Conditions
					</Checkbox>
					<Button
						style={{ backgroundColor: "#172b4d", color: "white", marginTop:"25px"}}
						htmlType="submit"
					>
						Create Account
					</Button>
					<div className="mt-5">
						Already have an account? <span onClick={()=>{handleSignIn()}} style={{cursor:"pointer", color:"blue"}}>Sign in</span>
					</div>
				</form>
			</Card>
		</>
	);
}
