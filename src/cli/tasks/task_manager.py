import json
import threading
from datetime import datetime

from src.cli.command import Command
from src.cli.structs.consts import JSON_DATABASE_PATH
from src.cli.tasks.task import Task

class TaskManager:

    def __init__(self, i_queue):
        self.q = i_queue
        self._running = True
        threading.Thread(target=self.run).start()
        self._mapping = {
            "add": self.add_task,
            "list": self.show_filter,
            "mark-in-progress": self.status_change,
            "mark-todo": self.status_change,
            "mark-done": self.status_change,
            "update": self.update_task,
            "delete": self.delete_task
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
    def show_filter(task_filter=None):
        try:
            with open(JSON_DATABASE_PATH, "r") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return

        if not task_filter:
            data_to_show = [task for task in data["tasks"] if data["tasks"]["status"] == task_filter]
        else:
            data_to_show = data["tasks"]
        print(data_to_show)


    @staticmethod
    def status_change(command: Command) -> None:
        pass

    @staticmethod
    def update_task(command: list) -> None:
        task_id, new_name = command
        file_path = JSON_DATABASE_PATH
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return

        for tasks in data["tasks"]:
            if tasks["task_id"] == int(task_id):
                tasks["description"] = new_name
                tasks["updated_at"] = datetime.now().isoformat()

        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)


    @staticmethod
    def add_task(task_desc: list[str]):
        file_path = JSON_DATABASE_PATH
        task = Task(*task_desc)

        try:
            with open(file_path, "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {"tasks": []}

        data["tasks"].append(task.__dict__)


        try:
            with open(file_path, "w") as file:
                json.dump(data, file, indent=4)
        except FileNotFoundError:
            print("NO DATABASE")
            return False

        print(f"Task id {task.task_id} added successfully")
        return True

    @staticmethod
    def delete_task(task_id: int) -> bool:
        task_id, = task_id
        file_path = JSON_DATABASE_PATH
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return False

        data["tasks"] = [task for task in data["tasks"] if task["task_id"] != int(task_id)]

        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)

        return True


