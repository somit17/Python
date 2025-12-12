import json
import os
FILE_NAME='tasks.json'


def print_menu():
    """Show Main Menu"""
    print("====== Personal Task Manager (Todo CLI) ======")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Mark task as complete")
    print("4. Delete a task")
    print("0. Exit")
    print("==============================================")

def load_tasks():
     if not os.path.exists(FILE_NAME):
         return []
     with open(FILE_NAME,mode='r') as json_reader:
         try:
             return json.load(json_reader)
         except json.JSONDecodeError:
             return []


def delete_task(tasks):
    idx = get_task_index(tasks,'delete')
    if idx is None:
        return

    deleted_task = tasks.pop(idx)
    save_tasks(tasks)
    print(f"Delete task successfully ! Description - {deleted_task['description']}\n")


def mark_task_completed(tasks):
    idx = get_task_index(tasks,action_name="mark as complete")
    if idx is None:
        return
    tasks[idx]['isCompleted']=True
    save_tasks(tasks)
    print(f"Task {idx+1} marked as completed")


def main():
    tasks=load_tasks()
    while True:
        print_menu()
        choice = input(f'Choose an option  : - ')

        if choice=='1':
            add_task(tasks)
        elif choice=='2':
            view_tasks(tasks)
        elif choice=='3':
            mark_task_completed(tasks)
        elif choice=='4':
            delete_task(tasks)
        elif choice=='0':
            print("Goodbye! 👋")
            break
        else:
            print("Invalid option. Please try again.\n")

def add_task(tasks):
    print('Add a new task with description and priority')
    description = input(f'Please enter the description\n')
    if not  description:
        print(f'Description cannot be empty.')
        return
    priority = input(f'Please enter the priority\n')
    if priority not in ('high','low','medium'):
        print(f'Priority cannot be empty.By default it will be set to "LOW"')
        priority='low'

    task = {
        'description':description,
        'priority':priority,
        'isCompleted':False
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f'Task Saved Successfully')


def save_tasks(tasks):
    with open(FILE_NAME,mode='w') as f:
        json.dump(tasks,f,indent=4)

def view_tasks(tasks):
    if not tasks:
        print(f'No Tasks found !\n')
        return
    print('Tasks : ')
    for i,task in enumerate(tasks,start=1):
        print(f"{i} ) Status - {task['isCompleted']} ** Description  - {task['description']} ** Priority - {task['priority']}\n")


def get_task_index(tasks,action_name):
    if not tasks:
        print(f'No tasks available.\n')
        return None
    view_tasks(tasks)
    choice = input(f"Enter task number to {action_name} : ")

    if not choice.isdigit():
        print("Please enter valid number")
        return  None
    idx = int(choice) - 1

    if idx < 0 or idx >= len(tasks):
        print("Invalid task number")
        return None
    return  idx

main()

