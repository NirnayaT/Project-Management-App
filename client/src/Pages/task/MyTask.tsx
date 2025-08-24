import { Collapse, CollapseProps, Divider, Dropdown,  } from 'antd';
import { CaretRightOutlined } from '@ant-design/icons';
import Todo from './Todo';
import Ongoing from './Ongoing';
import Completed from './Completed';
import '../../Theme/Css/MyTask.css'

const { Panel } = Collapse;

 const todoContent = (
  <Todo/>

 );


const ongoingContent = (
  <Ongoing/>
);

const completedContent = (
  <Completed/>
);
const MyTask = () => {
  return (
    <div className='bg-white mt-6 pt-4  px-4'>
        <div className="tabletitle">
        <div className="Head grid grid-cols-4  titleFont font-semibold mt-4 mb-5 ">
          
          <div className="bg-gray-200 ps-[100px] p-3 ">ID</div>
          <div className="bg-gray-200 py-3 ps-10">Task</div>
          <div className="bg-gray-200  py-3 ps-10">Priority</div>
          <div className="bg-gray-200 py-3 ps-10 ">Due Date </div>
        </div>
        <div className='main '>
        {todoContent}
        </div>
        

       

        </div>

    </div>
  )
}

export default MyTask
