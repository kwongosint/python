#Ask user for name and stores in variable called user_name
name = input("What is your name? ")
print("Hello " + name + "! Welcome to Task manager.")

birth_year = input("What year were you born? ")
current_year = 2026
age = current_year - int(birth_year)
print("You are " + str(age) + " years old.")

if age >= 18:
    print("You are an adult!")
else: 
    print("You are still a minor!")

tasks = ["email boss", "buy milk", "go to gym"]
print("Your tasks for today are: " + ", ".join(tasks))

new_task = input("What task would you like to add? ")
tasks.append(new_task)
print("Your updated list of tasks for today are: " + ", ".join(tasks))

while True:
    new_task = input("What task would you like to add? (type 'done' to finish) ")
    if new_task.lower() == 'done':
        break
    tasks.append(new_task)
print("Your final list of tasks for today are: " + ", ".join(tasks))
