from datetime import datetime


class Task(object):

    task_id = 0

    def __init__(self, description: str, status: str = "TODO"):
        self.description = description
        self.status = status
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        Task.task_id += 1

    async def update(self, status) -> None:
        self.status = status
        self.updated_at = datetime.now()

    def __str__(self):
        return f"Task {self.description} | status: {self.status} | ID: {self.task_id} | Created: {self.created_at}"




