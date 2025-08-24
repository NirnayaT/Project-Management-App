import React from 'react'
import { Draggable } from 'react-beautiful-dnd';

const Container= styled.div`
border-radius:10px;
padding:8px;
color:#000;
margin-bottom:8px;
margin-left:10px;
margin-right:10px;
min-height:90px;
cursor:pointer;
display:flex;
justify-content:space-between;
flex-directiom:column;
`;
export default function TaskList  ({task,index})  {
  return (
    <Draggable draggableId={`${task.id}`} key={task.id} index={index}>
          {(provided,snapshot)=>(
               <Container
                    {...provided.draggableProps}
                    {...provided.dragHandleProps}
                    ref={provided.innerRef}
                    isDragging={snapshot.isDragging}
               >
               </Container>
          )}

    </Draggable>
  )
}

