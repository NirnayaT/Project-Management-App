
import { ConfigProvider } from 'antd'
import { ReactNode } from 'react'
import SelectedTheme from './selectedTheme';
import { ThemeProvider } from 'styled-components';
import theme from '.';
interface customeProps{
  children:ReactNode;
}
const CustomThemeContext = ({children}:customeProps) => {
  return (
    <>
    <ThemeProvider theme={theme.selectedTheme}>
      <ConfigProvider
            theme={{
              token: {
                colorPrimary:SelectedTheme.Colors.primary?.p3,
                colorSuccess: SelectedTheme.Colors.success.s3,
                colorError: SelectedTheme.Colors.error.e3,
                colorInfo: SelectedTheme.Colors.link.l3,
                colorWarning: SelectedTheme.Colors.warning.w3,
                colorText: SelectedTheme.Colors.text.t7,
                colorTextDisabled: SelectedTheme.Colors.text.t2,
                // colorBgBase:SelectedTheme.Colors.background.b5,
      
              },
              components: {
                Card:{
                  colorBgBase:"#fff"
                },
                Button: {
                  // size
                  controlHeightSM: 36,
                  controlHeight: 40,
                  controlHeightLG: 44,
                  paddingInlineSM: 12,
                  paddingInline: 14,
                  paddingInlineLG: 16,
                  defaultBorderColor:"#f0f2f5",
                  defaultBg:'#f0f2f5',
                  // border
                  borderRadiusSM: 10,
                  borderRadius: 11,
                  borderRadiusLG: 12,
                  // font
                  fontWeight: 450,
                  contentFontSizeSM: 15,
                  contentFontSize: 15,
                  contentFontSizeLG: 16,
                  contentLineHeightSM: 1.334,
                  contentLineHeight: 1.334,
                  contentLineHeightLG: 1.25,
                  // icon
                  onlyIconSizeSM: 20,
                  onlyIconSize: 20,
                  onlyIconSizeLG: 24,
                  marginXS: 6,
                  // default hover
                  defaultHoverBg: "#dcdcdc",
                   defaultHoverBorderColor: "none",
                  // defaultHoverColor: "white"
                },
                Input:{
                  hoverBorderColor:"#172b4d",
                  activeBorderColor:"#172b4d",
                  
                },
                Menu:{
                  itemActiveBg:"red"
                },
                InputNumber:{
                  activeShadow:"none",
                  activeBorderColor:"blue",
                  colorBorder:"none",
                },
                Select:{
                  optionActiveBg:"none",
                  optionSelectedBg:"none",
                  selectorBg:"none",
                  colorBorder:"none",
                  controlOutlineWidth	:0,
               }
            }}}
          >
            {children}
      </ConfigProvider>
    </ThemeProvider>
      
    </>
  )
}

export default CustomThemeContext

