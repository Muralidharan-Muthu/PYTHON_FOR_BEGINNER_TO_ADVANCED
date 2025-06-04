tasks = []

def add_task(task):
    tasks.append(task)
    print(f"'{task}' added!")

def delete_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"'{task}' removed!")
    else:
        print("Task not found!")

def show_tasks():
    if tasks:
        print("Your Tasks:")
        for t in tasks:
            print("-", t)
    else:
        print("No tasks to show!")

# Testing our manager
add_task("Learn Python")
add_task("Watch movie")
show_tasks()
delete_task("Watch movie")
show_tasks()
