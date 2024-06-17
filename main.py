from functions import *
from services import create_task,display_tasks, remove_task


while True:
    _input = int(input("""
            *************TO DO APP USING CLI************
            *       1. Add tasks                       *
            *       2. Remove tasks                    *
            *       3. Show tasks                      *
            *       4. Exit                            *
            ******************************************** 
    ------> """))


    if _input == 1:
        create_task()#from services.py
    elif _input == 2:
        remove_task()#from services.py
    elif _input == 3:
        display_tasks()#from services.py
    elif _input == 4:
        break #while-loop breaks