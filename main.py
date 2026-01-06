#!/usr/bin/env python3
"""
Todo App - CLI Todo Application

This application was generated from specifications following Hackathon II rules.
It implements a simple in-memory CLI Todo application with the following features:
- Add Task
- View Tasks
- Update Task
- Delete Task
- Mark Task as Complete
"""

import json
from datetime import datetime
from typing import Dict, List, Optional


class Task:
    """Represents a single task in the todo list."""
    
    def __init__(self, task_id: int, description: str, completed: bool = False, due_date: Optional[str] = None):
        self.id = task_id
        self.description = description
        self.completed = completed
        self.due_date = due_date
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def to_dict(self):
        """Convert task to dictionary for serialization."""
        return {
            'id': self.id,
            'description': self.description,
            'completed': self.completed,
            'due_date': self.due_date,
            'created_at': self.created_at
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        """Create a Task instance from a dictionary."""
        task = cls(
            task_id=data['id'],
            description=data['description'],
            completed=data.get('completed', False),
            due_date=data.get('due_date')
        )
        task.created_at = data.get('created_at', '')
        return task


class TodoApp:
    """Main Todo application class."""
    
    def __init__(self):
        self.tasks: Dict[int, Task] = {}
        self.next_id = 1
    
    def add_task(self, description: str, due_date: Optional[str] = None) -> Optional[Task]:
        """
        Add a new task to the todo list.
        
        Args:
            description: Task description (required)
            due_date: Optional due date in YYYY-MM-DD format
            
        Returns:
            Task object if successful, None otherwise
        """
        # Validate input
        if not description or description.strip() == "":
            print("Error: Task description cannot be empty or whitespace only")
            return None
        
        if len(description) > 500:
            print("Error: Task description must be less than 500 characters")
            return None
        
        # Validate date format if provided
        if due_date:
            try:
                datetime.strptime(due_date, "%Y-%m-%d")
            except ValueError:
                print("Error: Invalid date format. Please use YYYY-MM-DD format")
                return None
        
        # Create new task
        task = Task(self.next_id, description.strip(), False, due_date)
        self.tasks[self.next_id] = task
        self.next_id += 1
        
        print(f"Task added successfully: ID {task.id} - {task.description}")
        return task
    
    def view_tasks(self, filter_status: Optional[str] = None) -> List[Task]:
        """
        View all tasks in the todo list.
        
        Args:
            filter_status: Optional filter ("all", "completed", "pending")
            
        Returns:
            List of tasks matching the filter
        """
        if not self.tasks:
            print("No tasks found")
            return []
        
        # Apply filter if specified
        if filter_status == "completed":
            filtered_tasks = [task for task in self.tasks.values() if task.completed]
        elif filter_status == "pending":
            filtered_tasks = [task for task in self.tasks.values() if not task.completed]
        else:
            filtered_tasks = list(self.tasks.values())
        
        if not filtered_tasks:
            print("No tasks found with the specified filter")
            return []
        
        # Display tasks
        print("\n--- Todo List ---")
        for task in sorted(filtered_tasks, key=lambda t: t.id):
            status = "✓" if task.completed else "○"
            due_info = f", Due: {task.due_date}" if task.due_date else ""
            print(f"{task.id}. [{status}] {task.description}{due_info}")
        print("-----------------\n")
        
        return filtered_tasks
    
    def update_task(self, task_id: int, new_description: Optional[str] = None, new_due_date: Optional[str] = None) -> bool:
        """
        Update an existing task's description or due date.
        
        Args:
            task_id: ID of the task to update
            new_description: New description (optional)
            new_due_date: New due date (optional)
            
        Returns:
            True if update was successful, False otherwise
        """
        if task_id not in self.tasks:
            print(f"Error: Task with ID {task_id} does not exist")
            return False
        
        task = self.tasks[task_id]
        
        # If both parameters are None, nothing to update
        if new_description is None and new_due_date is None:
            print("Error: No fields to update provided")
            return False
        
        # Update description if provided
        if new_description is not None:
            if not new_description or new_description.strip() == "":
                print("Error: Task description cannot be empty or whitespace only")
                return False
            task.description = new_description.strip()
        
        # Update due date if provided
        if new_due_date is not None:
            if new_due_date.strip() == "":
                # Empty string means clear the due date
                task.due_date = None
            else:
                try:
                    datetime.strptime(new_due_date, "%Y-%m-%d")
                    task.due_date = new_due_date
                except ValueError:
                    print("Error: Invalid date format. Please use YYYY-MM-DD format")
                    return False
        
        print(f"Task updated successfully: ID {task.id} - {task.description}")
        return True
    
    def delete_task(self, task_id: int) -> bool:
        """
        Delete an existing task from the todo list.
        
        Args:
            task_id: ID of the task to delete
            
        Returns:
            True if deletion was successful, False otherwise
        """
        if task_id not in self.tasks:
            print(f"Error: Task with ID {task_id} does not exist")
            return False
        
        task = self.tasks[task_id]
        del self.tasks[task_id]
        print(f"Task deleted successfully: ID {task.id} - {task.description}")
        return True
    
    def mark_task_complete(self, task_id: int, completed: bool) -> bool:
        """
        Mark an existing task as complete or incomplete.
        
        Args:
            task_id: ID of the task to update
            completed: True to mark as complete, False to mark as incomplete
            
        Returns:
            True if update was successful, False otherwise
        """
        if task_id not in self.tasks:
            print(f"Error: Task with ID {task_id} does not exist")
            return False
        
        task = self.tasks[task_id]
        task.completed = completed
        status_text = "completed" if completed else "incomplete"
        print(f"Task marked as {status_text}: ID {task.id} - {task.description}")
        return True
    
    def run(self):
        """Run the main application loop."""
        print("Welcome to the Todo App!")
        print("Available commands:")
        print("  add <description> [due_date] - Add a new task")
        print("  view [all|completed|pending] - View tasks")
        print("  update <id> [new_description] [new_due_date] - Update a task")
        print("  delete <id> - Delete a task")
        print("  complete <id> - Mark task as complete")
        print("  incomplete <id> - Mark task as incomplete")
        print("  quit - Exit the application")
        print()
        
        while True:
            try:
                command = input("Enter command: ").strip().split()
                
                if not command:
                    continue
                
                cmd = command[0].lower()
                
                if cmd == "quit":
                    print("Goodbye!")
                    break
                elif cmd == "add":
                    if len(command) < 2:
                        print("Usage: add <description> [due_date]")
                        continue
                    description = command[1]
                    due_date = command[2] if len(command) > 2 else None
                    self.add_task(description, due_date)
                elif cmd == "view":
                    filter_status = command[1] if len(command) > 1 else None
                    if filter_status and filter_status not in ["all", "completed", "pending"]:
                        print("Filter must be 'all', 'completed', or 'pending'")
                        continue
                    self.view_tasks(filter_status)
                elif cmd == "update":
                    if len(command) < 3:
                        print("Usage: update <id> [new_description] [new_due_date]")
                        continue
                    try:
                        task_id = int(command[1])
                        new_description = command[2] if len(command) > 2 and command[2] != "None" else None
                        new_due_date = command[3] if len(command) > 3 and command[3] != "None" else None
                        self.update_task(task_id, new_description, new_due_date)
                    except ValueError:
                        print("Task ID must be a number")
                elif cmd == "delete":
                    if len(command) < 2:
                        print("Usage: delete <id>")
                        continue
                    try:
                        task_id = int(command[1])
                        self.delete_task(task_id)
                    except ValueError:
                        print("Task ID must be a number")
                elif cmd == "complete":
                    if len(command) < 2:
                        print("Usage: complete <id>")
                        continue
                    try:
                        task_id = int(command[1])
                        self.mark_task_complete(task_id, True)
                    except ValueError:
                        print("Task ID must be a number")
                elif cmd == "incomplete":
                    if len(command) < 2:
                        print("Usage: incomplete <id>")
                        continue
                    try:
                        task_id = int(command[1])
                        self.mark_task_complete(task_id, False)
                    except ValueError:
                        print("Task ID must be a number")
                else:
                    print("Unknown command. Available commands: add, view, update, delete, complete, incomplete, quit")
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except EOFError:
                print("\nGoodbye!")
                break


def main():
    """Main entry point."""
    app = TodoApp()
    app.run()


if __name__ == "__main__":
    main()