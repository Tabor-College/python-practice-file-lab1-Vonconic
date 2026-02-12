task_list = []


while True:
    initial_input = input("Enter tasks you want to add to the list (type done to finish): ")
    
    if initial_input == "done":
        break
    
    task_list.append(initial_input)


while True:
    user_input = int(input(
    """
    1. Add a new task
    2. Insert a task at a position
    3. Remove a task by name
    4. Remove a task by index
    5. Update a task
    6. View all tasks
    7. Sort tasks
    8. Reverse tasks
    9. Search for a task
    10. Task statistics
    11. Copy task list
    12. Clear all tasks
    13. Exit
    
    Enter option number to select: """
    ))
    
    # index is the internal order of a list and everything in a list has a indext labeled 

    if user_input == 1:
        while True:
            initial_input = input("Enter tasks you want to add to the list (type done to finish): ")
    
            task_list.append(initial_input)
    
            if initial_input == "done":
                break

    if user_input == 2:
        
        while True:

            for index, task in enumerate(task_list):
                print(f"Index {index}: {task}")
            


            task = input("name of the task you want to add (type return to exit): ")
            
            if task == "return":
                break
            
            index = int(input("Enter the index at which you want to add the task: "))
            

            task_list.insert(index, task)

            

    #remove() removes things by name and pop() removes things by index
    
    if user_input == 3:
        
        while True:
            
            for task in task_list:
                print(task)
            
            task_to_remove = str(input("Enter the name of the task you want to remove: "))
            
            if task_to_remove == "return":
                break

            if task_to_remove in task_list:
                task_list.remove(task_to_remove)
                print (f"Task {task_to_remove} removed")
            else:
                print("Task not in list")

    if user_input == 4:
        while True:
            for index, task in enumerate(task_list):
                print(f"Index {index}: {task}")

            index_option = int(input("Enter the index of the task you want to remove (type -1 to exit): "))

            if index_option == -1:
                break
        
            if 0 <= index_option < len(task_list):
                task_list.pop(index_option)
            else:
                print("Task does not exist at this index")
            
    if user_input == 5:
        while True:
            for index, task in enumerate(task_list):
                print(f"Index {index}: {task}")

            index_input = int(input("Enter the index of the task you want to change (type -1 to exit): "))

            if index_input == -1:
                break

            if 0 <= index_input < len(task_list):
                rename_input = input("Enter the new name of the task (Type return to exit): ")
                
                if rename_input == "return":
                    break

                task_list[index_input] = rename_input
            else:
                print("Task does not exist at this index")
        

    if user_input == 6:

        while True:
            for index, task in enumerate(task_list):
                print(f"Index {index}: {task}")

            option = input("type return to go back: ")
            if option == "return":
                break
    

    # When sort() is used things are sorted alphabetically or numerically depending on the value

    if user_input == 7:
        while True:
            
            task_list = sorted(task_list)
            print(task_list)
            print("Task list sorted alphabetically")

            option_sorted = input("Type return to go back: ")
            if option_sorted == "return":
                break

    if user_input == 8:

        while True:
            
            task_list.reverse()
            print(task_list)

            option_reversed = input("Type return to go back: ")
            if option_reversed == "return":
                break 

    if user_input == 9:
        
        while True:
            task_search = str(input("Search for a task: "))   
            if task_search in task_list:
                task_count = task_list.count(task_search)
                task_index = task_list.index(task_search)

                print(f"{task_count} result(s) found at index {task_index}")
            option_search = input("Type return to exit: ")
            if option_search == "return":
                break
    

    if user_input == 10:
        while True:
        
            task_stats = int(input("""
            1. Total number of tasks
            2. First task
            3. Last task 
            4. Exit    
            Enter option number: """))

            if task_stats == 1:
                print(f"There are {len(task_list)} tasks in this list")
            
            if task_stats == 2:
                print(f"The first item in this list is {task_list[0]}") 

            if task_stats == 3:
                print(f"The last item in this list {task_list[len(task_list) - 1]}")
            
            if task_stats == 4:
                break

    # copying is safter than (=) because it creates a completely independent obect

    if user_input == 11:
        while True:
            copied_list = task_list.copy()
            print(copied_list)
            option_copy = input("type return to exit")
            if option_copy == "return":
                break
    
    if user_input == 12:
    
        while True:
            certain = input("Are you sure you would like to clear the list? (Yes to delete or No to exit): ")
            if certain == "Yes":
                task_list.clear()
            
            if certain == "No":
                break

    if user_input == 13:
        break
