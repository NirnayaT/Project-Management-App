from enum import Enum


class TaskStatus(Enum):
    """
    Defines the possible status values for a task.
    
    TODO: The task is not started yet.
    INPROGRESS: The task is currently being worked on.
    FINISHED: The task has been completed.
    """
        
    TODO = "TODO"
    INPROGRESS = "INPROGRESS"
    FINISHED = "FINISHED"
    

class TaskPriority(Enum):
    """
        Defines the possible priority levels for a task.
        
        LOW: The task has a low priority.
        MEDIUM: The task has a medium priority.
        HIGH: The task has a high priority.
        """
        
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"