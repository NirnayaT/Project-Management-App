import React from "react";

import { Input } from "antd";
import { MailOutlined } from "@ant-design/icons";
import { Controller } from "react-hook-form";

interface PasswordInputProps {
	errors?: string;
	// eslint-disable-next-line @typescript-eslint/no-explicit-any
	// field:ControllerRenderProps <any, 'password'>;
	size?: "large" | "default" | "small";
	placeholder?: string;
	prefix?: React.ReactNode;
	// eslint-disable-next-line @typescript-eslint/no-explicit-any
	control: any;
	name: string;
}
const PasswordInput: React.FC<PasswordInputProps> = ({
	// field,
	control,
	errors,
	size = "default",
	placeholder = "********",
	prefix = <MailOutlined />,
	name,
}) => (
	<div className="email mb-4">
		{!control && (
			<Input.Password
				control={control}
				size={size}
				placeholder={placeholder}
				className="ps-2"
				prefix={prefix}
			/>
		)}
		{control && (
			<Controller
				// {...field}
				name={name}
				control={control}
				render={({ field }) => {
					return (
						<Input.Password
							{...field}
							name={name}
							size={size}
							placeholder={placeholder}
							type="password"
							prefix={prefix}
							className="ps-2"
						/>
					);
				}}
			/>
		)}
		{errors && <p className="text-[red]">{errors}</p>}
	</div>
);
export default PasswordInput;
