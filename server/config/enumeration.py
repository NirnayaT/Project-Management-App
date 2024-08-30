from enum import Enum


class TaskStatus(Enum):
    TODO = "TODO"
    INPROGRESS = "INPROGRESS"
    FINISHED = "FINISHED"
    

class TaskPriority(Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"