task_file = "tsk.txt"

def task_load():
    try:
        with open(task_file, "r") as file:
            return file.read.splitlines()
    except FileNotFoundError:
        return []

def save_task(tasks):
    with open(task_file, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def display_task(tasks):

    if not tasks:
        print("Nothing to show.")
        return 
    
    for i, task in enumerate(tasks, start=1):
        print(f"{i}: {task}")
