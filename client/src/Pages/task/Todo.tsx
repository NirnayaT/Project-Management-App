import { Divider } from 'antd'
import { useGetTaskUser } from './common/useGetTask'


export default function Todo ()  {
  const {data: task} = useGetTaskUser()
  console.log(task, "cccccccccccccc")
  return (
     <>
     {task?.map((task) => (
                  <div className="taskList grid grid-cols-7 ms-2 pt-[28px] pb-[28px] "  >
                    <div className="ms-[80px] w-fit " >{task?.id}</div>
                    <div className="ms-[9rem] w-[20rem] ">{task?.task}</div>
                    <div className="ms-[19rem]">{task?.priority}</div>
                    <div className="ms-[28rem] w-[10rem]">{task?.due_date}</div>
                    
     
                  </div>
          ))}
     </>
  )
}
