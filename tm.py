task_file = "tsk.txt"

def task_load():
    try:
        with open(task_file, "r") as file:
            return file.read.splitlines()
    except FileNotFoundError:
        return []

def save_task(tasks):
    with open(task_file, "r") as file:
        for i in tasks:
            file.write(i)