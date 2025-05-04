import json
import threading
from queue import Queue

from src.cli.command import Command
from src.cli.tasks.task import Task
from asyncio import run

class TaskManager:

    def __init__(self, i_queue):
        self.q = i_queue
        self._running = True
        threading.Thread(target=self.run).start()
        self._mapping = {
            "add": self.add_task,
            "list": None,
            "mark-in-progress": None,
            "mark-todo": None,
            "mark-done": None,
            "update": None,
            "delete": None
        }

    def run(self) -> None:
        while self._running:
            data = self.q.get()
            # TODO: ADD DATA VALIDATION
            new_command = Command(data[0], data[1:])
            self._mapping[new_command.command](new_command.args)

    def stop(self) -> None:
        self._running = False

    @staticmethod
    def add_task(task_desc: list[str]):
        file_path = "src/database/json_database.json"
        task = Task(*task_desc)

        # Step 1: Read file safely
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {"tasks": []}

        # Step 2: Append new task
        data["tasks"].append(task.__dict__)

        # Step 3: Write entire structure back to file
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)

        print(f"Task id {task.task_id} added successfully")
