from database import show_task, add_task, TaskRepository

_input = int(input("""
         *************TO DO APP USING CLI************
         *       1. Add tasks                       *
         *       2. Remove tasks                    *
         *       3. Show tasks                      *
         *       4. Exit                            *
         ******************************************** 
------> """))


if _input == 1:
    # task = get_task_from_user()
    add_task()
elif _input == 2:
    print("task removes")
elif _input == 3:
    show_task()
elif _input == 4:
    exit()