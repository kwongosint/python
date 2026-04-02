# 1. DATA INITIALIZATION
# We start with an empty list. This is our 'in-memory' database.
tasks = [] 

# 2. THE MAIN GAME LOOP
# while True creates a loop that never ends unless we hit a 'break' command.
# This keeps the app running after every action.
while True:
    print("\n--- MENU ---")
    print("1. Show Tasks | 2. Add Task | 3. Remove Task | 4. Exit")
    
    # input() always captures data as a STRING. 
    # We compare choice to "1" (string) instead of 1 (number).
    choice = input("What would you like to do? (1-4) ")

    # 3. READ (Show Tasks)
    if choice == "1":
        # len() checks the size of the list. 0 means it's empty.
        if len(tasks) == 0:
            print("Your task list is empty!")
        else:
            print("\n--- CURRENT TASKS ---")
            count = 1
            # Iterating through the list using a 'for' loop
            for task in tasks:
                # capitalize() makes it look clean. 
                # str(count) is needed to combine numbers with text.
                print(str(count) + ". " + task.capitalize())
                count += 1

    # 4. CREATE (Add Task)
    elif choice == "2":
        new_task = input("Enter the task you want to add: ")
        # Validation: Checking if the user just hit enter (empty string)
        if new_task == "":
            print("You can't add an empty task!")
        else:
            tasks.append(new_task)
            # f-strings (f"...") allow us to inject variables directly into text using {}
            print(f"'{new_task}' has been added.")

    # 5. DELETE (Remove Task)
    elif choice == "3":
        if len(tasks) == 0:
            print("Nothing to remove!")
        else:
            # We show the list first so the user knows which number to pick
            print("\n--- CURRENT TASKS ---")
            for i, task in enumerate(tasks, 1): # enumerate is a fancy way to get index + item
                print(f"{i}. {task.capitalize()}")
            
            choice_num = input("\nEnter the number to remove: ")
            
            # int() conversion is risky if user types a letter (will crash)
            # but for now, we assume they type a number.
            index_to_remove = int(choice_num) - 1
            
            # BOUNDS CHECKING: 
            # This ensures the number is actually inside our list range.
            if 0 <= index_to_remove < len(tasks):
                # .pop() removes the item and returns it to us.
                removed_task = tasks.pop(index_to_remove)
                print(f"'{removed_task}' has been removed.")
            else:
                print("Invalid choice! That task number doesn't exist.")

    # 6. PERSISTENCE (Save & Exit)
    elif choice == "4":
        # 'with open' automatically closes the file for us when finished.
        # "w" mode means 'write' (it overwrites the file).
        with open("tasks.txt", "w") as file:
            for task in tasks:
                # \n ensures each task is on a new line in the text file.
                file.write(task + "\n")
        
        print("Tasks saved to tasks.txt! Goodbye!")
        break # This is the only way out of the 'while True' loop.

    # 7. CATCH-ALL (Error Handling)
    else:
        print("Invalid choice! Please enter 1, 2, 3, or 4.")