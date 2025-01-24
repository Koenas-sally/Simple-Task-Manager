# Task Manager

This Python-based Task Manager application allows users to efficiently manage their tasks with features like adding, listing, sorting, marking tasks as completed, and checking deadlines. The program utilizes a `Task` class for individual tasks and a `TaskManager` class for managing the list of tasks.

---

## Features

### 1. Add Task
Allows users to add a new task with the following properties:
- **Title**: The name of the task (cannot be empty).
- **Description**: Additional details about the task.
- **Due Date**: The deadline for the task in `YYYY-MM-DD` format (validated).
- **Priority**: A number between 1 (highest) and 5 (lowest).
- **Completion Status**: Automatically set to "Pending" upon creation.

### 2. List Tasks
Displays a table of all tasks, showing:
- Index
- Title
- Due Date
- Priority
- Status (Completed/Pending)

### 3. Mark Task as Completed
Allows the user to mark a specific task as completed based on its index.

### 4. Check Deadlines
Highlights tasks with approaching deadlines:
- **Overdue Tasks**: Tasks with due dates earlier than the current date.
- **Due Soon Tasks**: Tasks with due dates within the next three days.

### 5. Sort Tasks
Users can sort tasks by:
- **Title**: Alphabetical order.
- **Due Date**: Chronological order.
- **Priority**: Ascending order (1 is the highest priority).

### 6. Save and Load Tasks *(Planned Feature)*
- Save tasks to a file in JSON format for persistence.
- Load tasks from a JSON file.

---

## Menu Options

The application provides the following menu options:

1. **Add Task**: Add a new task.
2. **List Tasks**: View all tasks in a table format.
3. **Remove Task** *(Planned Feature)*: Delete a specific task by index.
4. **Update Task** *(Planned Feature)*: Modify details of an existing task.
5. **Search Task** *(Planned Feature)*: Search for tasks by title.
6. **Mark Task as Completed**: Update the completion status of a task.
7. **Check Deadlines**: Identify overdue and near-due tasks.
8. **Sort Tasks**: Organize tasks by title, due date, or priority.
9. **Save Tasks** *(Planned Feature)*: Save tasks to a JSON file.
10. **Load Tasks** *(Planned Feature)*: Load tasks from a JSON file.
11. **Exit**: Exit the application.

---

## Getting Started

### Prerequisites
- Python 3.x installed on your system.

### How to Run
1. Save the script to a file (e.g., `task_manager.py`).
2. Open a terminal or command prompt.
3. Run the script using:
   ```bash
   python task_manager.py
   ```
4. Follow the on-screen menu to interact with the application.

---

## Code Highlights

### Task Class
Handles individual task properties and provides a `to_dict` method for easy serialization:
```python
class Task:
    def __init__(self, title, description, due_date, priority, completed=False):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = completed

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "priority": self.priority,
            "completed": self.completed,
        }
```

### TaskManager Class
Manages a list of tasks and implements operations like adding, listing, and sorting tasks.

### Error Handling
- Validates input for dates (`YYYY-MM-DD`) and priority (1-5).
- Handles invalid menu choices and input errors gracefully.

---

## Planned Enhancements
1. **Remove Task**: Allow users to delete tasks by index.
2. **Update Task**: Enable editing of task details.
3. **Search Task**: Search for tasks by title.
4. **Save and Load Tasks**: Add persistence using JSON files.

---

## Example Interaction
```
Task Manager Menu:
1. Add Task
2. List Tasks
3. Remove Task
4. Update Task
5. Search Task
6. Mark Task as Completed
7. Check Deadlines
8. Sort Tasks
9. Save Tasks
10. Load Tasks
11. Exit
Enter your choice: 1
Enter task title: Finish Homework
Enter task description: Complete math and science assignments.
Enter task due date (YYYY-MM-DD): 2025-01-30
Enter task priority (1-5): 2
Task added successfully!
```

---

## License
This project is open-source and available for personal and educational use.

