task_file = "tsk.txt"

def task_load():
    try:
        with open(task_file, "r") as file:
            return file.read.splitlines()