
from datetime import date

class TaskStore:
    def __init__(self):
        self.tasks = [
            {"id": 1, "title": "Prepare report", "status": "pending", "due_date": "2026-11-01"},
            {"id": 2, "title": "Review pull request", "status": "in_progress", "due_date": "2026-11-03"},
            {"id": 3, "title": "Deploy application", "status": "completed", "due_date": "2026-10-20"},
        ]
        self.next_id = 4

    def list_tasks(self, status=None):
        if status is None:
            return self.tasks.copy()
        return [task for task in self.tasks if task["status"] == status]

    def create_task(self, title, due_date):
        if not title.strip():
            raise ValueError("Title cannot be empty")
        date.fromisoformat(due_date)
        task = {
            "id": self.next_id,
            "title": title.strip(),
            "status": "pending",
            "due_date": due_date,
        }
        self.tasks.append(task)
        self.next_id += 1
        return task

    def update_status(self, task_id, status):
        if status not in {"pending", "in_progress", "completed"}:
            raise ValueError("Invalid task status")
        for task in self.tasks:
            if task["id"] == task_id:
                task["status"] = status
                return task
        raise KeyError("Task not found")
