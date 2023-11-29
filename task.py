name=input("Enter your Name:")

tasks = []
def add_task(task):
    tasks.append(task)
    print(f"\nTask :'{task}' added to the list.")

def display_tasks():
    if tasks:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"\n{index}. {task}")
    else:
        print("\nNo tasks in the list.")

def remove_task(index):
    if 1 <= index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        print(f"\nTask '{removed_task}' removed from the list.")
    else:
        print("\nInvalid task index.")
print("\n------- Welcome to The To-Do List Application ",name,"--------\n")
while True:
    
    print("\n\t****Main Menu of To Do list****")
    print("\n\t1. Add a task   2. Display tasks \n\t3. Remove task   4. Quit")
  
    choice = input("Enter your choice: ")
    
    if choice == '1':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '2':
        display_tasks()
    elif choice == '3':
        index = int(input("Enter the task index to remove: "))
        remove_task(index)
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
