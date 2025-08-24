import { Card } from 'antd';
interface CardProps{
  title:string;
  content:string;
  className:string;
  width?:number;
}
const Cards:React.FC<CardProps> =(
  {
    title="Enter Title",
    content="Enter Content",
    className="ps-2",
    width
  }
)=>
{
return(
    <Card
      title={title}
      content={content}
      bordered={false}
      className={className}
      style={{ width}}
    >
      <p>{content}</p>
    </Card>
  )
}
export default Cards
