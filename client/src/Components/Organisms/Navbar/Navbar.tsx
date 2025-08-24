import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"
import { faBell, faUser, faGear } from "@fortawesome/free-solid-svg-icons";
import { Dropdown, MenuProps, Tooltip } from 'antd';
import { useNavigate } from "react-router-dom";
export default function Navbar() {
  const navigate = useNavigate();
  const handleLogout = () => {
    localStorage.removeItem("access_token");
    localStorage.removeItem("refresh_token");
    navigate("/");
  };
  const handleProfile = () => {
    navigate("/profile");
  };
  const items: MenuProps['items'] = [
    {
      label: <a onClick={handleProfile}>Profile</a>,
      key: '0',
    },
    {
      label: <a href="https://www.aliyun.com">Setting</a>,
      key: '1',
    },
    {
      type: 'divider',
    },
    {
      label: <a onClick={handleLogout}>Logout</a>,
      key: '3',
    },
  ];
  return (
    <div className="flex justify-end">
      <Tooltip title={"notification"} className="me-10 mt-6" style={{ cursor: "pointer" }}>
        <FontAwesomeIcon icon={faBell} />
      </Tooltip>
      <Tooltip title={"setting"} className="me-10 mt-6" style={{ cursor: "pointer" }}>
        <FontAwesomeIcon icon={faGear} />
      </Tooltip>
      <Dropdown menu={{ items }} trigger={['click']}>
        <a onClick={(e) => e.preventDefault()}>
          <FontAwesomeIcon icon={faUser} className="me-5" />
        </a>
      </Dropdown>
    </div>
  )
}