# --- PHASE 1: USER GREETING & DATA TYPES ---

# input() always returns a String (text)
name = input("What is your name? ")
print("Hello " + name + "! Welcome to Task manager.")

birth_year = input("What year were you born? ")
current_year = 2026

# int() converts a String into an Integer so we can do math
age = current_year - int(birth_year)
print("You are " + str(age) + " years old.")

# --- PHASE 2: CONDITIONALS (IF/ELSE) ---

if age >= 18:
    print("You are an adult!")
else: 
    print("You are still a minor!")

# --- PHASE 3: LISTS & LOOPS ---

# Initializing our list with some starting data
tasks = ["email boss", "buy milk", "go to gym"]

# while True creates an infinite loop that runs until we 'break'
while True:
    new_task = input("What task would you like to add? (type 'done' to finish) ")
    
    # .lower() ensures "DONE" or "Done" both trigger the break
    if new_task.lower() == 'done':
        break
    
    # Simple validation: if the user just hits enter, skip this turn
    if new_task == "":
        continue
        
    # .append() adds the item to the very end of the list
    tasks.append(new_task)

# --- PHASE 4: FUNCTIONS ---

# This function takes one argument (task_list) and prints it nicely
def show_tasks(task_list):
    print("\n--- CURRENT TASKS ---")
    count = 1
    for task in task_list:
        # .capitalize() makes the first letter uppercase for better UI
        print(str(count) + ". " + task.capitalize())
        count += 1

# Call the function for the first time
show_tasks(tasks)

# --- PHASE 5: REMOVING DATA ---

# We ask for a number, convert to int, then subtract 1
# (Subtracting 1 because Python lists start at 0, but users start at 1)
choice = input("\nEnter the number of a task you finished to remove it: ")
#\n mea
index_to_remove = int(choice) - 1

# .pop() removes the item at that specific index position
tasks.pop(index_to_remove)

# Check if the list is empty using len()
if len(tasks) == 0:
    print("Congratulations! You have completed all your tasks for today!")
else:
    # Show the list one last time to confirm it's gone
    show_tasks(tasks)

with open("tasks.txt", "w") as file: 
    #"w" means we are opening the file in write mode, which will create it if it doesn't exist or overwrite it if it does
    for task in tasks:
        file.write(task + "\n")
print("Tasks saved to tasks.txt!")