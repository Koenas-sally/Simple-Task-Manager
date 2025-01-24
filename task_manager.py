import json


class Task:
    def __init__(self, title, description, due_date, priority):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "priority": self.priority,
        }

    @classmethod
    def from_dict(cls, task_dict):
        return cls(
            task_dict["title"],
            task_dict["description"],
            task_dict["due_date"],
            task_dict["priority"],
        )


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, due_date, priority):
        task = Task(title, description, due_date, priority)
        self.tasks.append(task)

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        for idx, task in enumerate(self.tasks, 1):
            print(f"{idx}. {task.title} | Due: {task.due_date} | Priority: {task.priority}")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            print("Task deleted successfully.")
        else:
            print("Invalid task index.")

    def save_tasks(self, filename="tasks.json"):
        with open(filename, "w") as file:
            json.dump([task.to_dict() for task in self.tasks], file)
        print("Tasks saved successfully.")

    def load_tasks(self, filename="tasks.json"):
        try:
            with open(filename, "r") as file:
                tasks = json.load(file)
                self.tasks = [Task.from_dict(task) for task in tasks]
        except FileNotFoundError:
            print("No saved tasks found.")


def main():
    manager = TaskManager()
    manager.load_tasks()

    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Delete Task")
        print("4. Save Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter title: ")
            description = input("Enter description: ")
            due_date = input("Enter due date: ")
            priority = int(input("Enter priority (1-5): "))
            manager.add_task(title, description, due_date, priority)

        elif choice == "2":
            manager.list_tasks()

        elif choice == "3":
            manager.list_tasks()
            index = int(input("Enter task index to delete: ")) - 1
            manager.delete_task(index)

        elif choice == "4":
            manager.save_tasks()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
