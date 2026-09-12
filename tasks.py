tasks = []

def add_task(name):
    tasks.append({
        "name": name,
        "completed": False
    })

def complete_task(name):
    for task in tasks:
        if task["name"] == name:
            task["completed"] = True
            return

def show_tasks():
    for task in tasks:
        status = "✓" if task["completed"] else " "
        print(f"[{status}] {task['name']}")


if __name__ == "__main__":
    add_task("Buy groceries")
    add_task("Go to gym")
    add_task("Study ML")
    add_task("Read a chapter of a book")
    add_task("Do laundry")
    add_task("Water the plants")
    add_task("Plan meals for the week")
    add_task("Practice Python")

    complete_task("Go to gym")

    show_tasks()
