import { Layout, Button, theme } from 'antd';
import {
  MenuFoldOutlined,
  MenuUnfoldOutlined,
} from '@ant-design/icons';
import { useState } from 'react';
import Navbar from '../Navbar/Navbar';

interface headerProps {
  collapse: () => void
  // collapsed:boolean
}
const { Header } = Layout;
const Headers: React.FC<headerProps> = ({ collapse }) => {
  const [col, setCol] = useState<boolean>(false)
  // console.log("collasped state>>",collapsed)
  const {
    token: { colorBgContainer },
  } = theme.useToken();
  const handleClick = (collapse: () => void) => {
    collapse();
    setCol(!col)
  }
  return (
    <>
      <Header style={{ padding: 0, background: colorBgContainer, display: "flex", justifyContent: "space-between", alignItems: "center" }}>
        <Button
          type="text"
          icon={col ? <MenuUnfoldOutlined /> : <MenuFoldOutlined />}
          onClick={() => { handleClick(collapse) }}
          style={{
            fontSize: '16px',
            width: 64,
            height: 64,
          }}
        />
        <Navbar />
      </Header>
    </>
  )
}

export default Headers
