import os
from datetime import datetime

from src.cli.utils.paths import get_path
from src.cli.utils.times import get_time


class Task(object):

    def __init__(self, description: str,  status: str = "todo"):
        self.description = description
        self.status = status
        self.created_at = get_time()
        self.updated_at = get_time()
        self.task_id = self.task_count()

    @staticmethod
    def task_count():
        """
        Gets and increases task count by 1
        :return:
        """
        path = get_path("../..", "database", "task_counter")
        with open(path, "r") as f:
            count = int(f.read())
        with open(path, "w") as f:
            count += 1
            f.write(str(count))
        return count

    def __str__(self):
        return f"Task {self.description} | status: {self.status} | ID: {self.task_id} | Created: {self.created_at}"
