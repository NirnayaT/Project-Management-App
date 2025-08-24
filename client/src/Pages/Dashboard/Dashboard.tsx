import {Row, Col, Calendar} from 'antd'
import type { Dayjs } from 'dayjs';
import { CalendarProps, Card } from 'antd';
import CardsTabs from "../../Components/Atoms/card/CardsTabs"
import { faCircleCheck, faCircleXmark, faClock, faFileLines } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
const onPanelChange = (value: Dayjs, mode: CalendarProps<Dayjs>['mode']) => {
  console.log(value.format('YYYY-MM-DD'), mode);
};
import Protected from '../../Routes/Protected';
const Dashboard = () => {


    return (
    <>
    {/* <div>

<div className="mt-7 ms-1 text-xl font-bold">
  Project Status
</div>
<div className=" flex gap-4 mb-2 mt-[30px]">
<Card style={{ width: 300 }}>
  <div className="flex justify-center mb-3">
  <FontAwesomeIcon icon={faCircleXmark} className="h-[27px]" style={{ color:"#E34234"}}/>
  </div>
  <p className="text-center font-bold text-xl" >Not Started</p>
  <p className="text-center">Card content</p>
</Card>
<Card style={{ width: 300 }} >
  <div className="flex justify-center mb-3">

    <FontAwesomeIcon icon={faCircleCheck} className="h-[27px]" style={{ color:"#90EE90"}}/>
  </div>
  <p className="text-center font-bold text-xl ">Completed</p>
  <p className="text-center">Card content</p>
</Card>
  <Card style={{ width: 300 }}>
  <div className="flex justify-center mb-3">
  <FontAwesomeIcon icon={faClock}  className="h-[27px]" style={{color:"#FFFF8F"}}/>
  </div>
  <p className="text-center font-bold text-xl">In Progress</p>
  <p className="text-center">Card content</p>
</Card>
<Card style={{ width: 300 }}>
<div className="flex justify-center mb-3">
<FontAwesomeIcon icon={faFileLines}  className="h-[27px]" style={{ color:"#54b0fc"}}/>
</div>
  <p className="text-center font-bold text-xl">Total</p>
  <p className="text-center">Card content</p>
</Card>
</div>
</div> */}
      <Row className="flex justify-between">
        <Col>
        <Card title="Task Status" bordered={false} style={{ width: 700 }}>
          <div className=" grid grid-cols-2 gap-y-3">

        <Card style={{ width: 300 }}>
        <div className="flex justify-center mb-3">
        <FontAwesomeIcon icon={faCircleXmark} className="h-[27px]" style={{ color:"#E34234"}}/>
        </div>
        <p className="text-center font-bold text-xl" >Not Started</p>
        <p className="text-center">Card content</p>
      </Card>
      <Card style={{ width: 300 }} >
        <div className="flex justify-center mb-3">

          <FontAwesomeIcon icon={faCircleCheck} className="h-[27px]" style={{ color:"#90EE90"}}/>
        </div>
        <p className="text-center font-bold text-xl ">Completed</p>
        <p className="text-center">Card content</p>
      </Card>
        <Card style={{ width: 300 }}>
        <div className="flex justify-center mb-3">
        <FontAwesomeIcon icon={faClock}  className="h-[27px]" style={{color:"#FFFF8F"}}/>
        </div>
        <p className="text-center font-bold text-xl">In Progress</p>
        <p className="text-center">Card content</p>
      </Card>
      <Card style={{ width: 300 }}>
      <div className="flex justify-center mb-3">
      <FontAwesomeIcon icon={faFileLines}  className="h-[27px]" style={{ color:"#54b0fc"}}/>
      </div>
        <p className="text-center font-bold text-xl">Total</p>
        <p className="text-center">Card content</p>
      </Card>
          </div>


        </Card>

        </Col>
        <Col>
        <Calendar fullscreen={false} onPanelChange={onPanelChange} className="mb-2 w-[500px] h-[390px]"/>
        </Col>
      </Row>
      <CardsTabs
      />

      
    </>

  )
}

export default Dashboard
