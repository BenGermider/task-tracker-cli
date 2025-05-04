import json
import threading
from datetime import datetime

from src.cli.command import Command
from src.cli.utils.consts import JSON_DATABASE_PATH
from src.cli.tasks.task import Task
from src.cli.utils.paths import get_path


class TaskManager:

    def __init__(self, ):
        self._mapping = {
            "add": self.add_task,
            "list": self.show_filter,
            "mark-in-progress": self.status_change,
            "mark-todo": self.status_change,
            "mark-done": self.status_change,
            "update": self.update_task,
            "delete": self.delete_task
        }

    def run(self, args) -> None:
        """
        Consumer of user input
        :return:
        """
        # TODO: ADD DATA VALIDATION
        new_command = Command(args[0], args[1:])
        if "mark" in new_command.command:
            self.status_change(new_command)
        else:
            self._mapping[new_command.command](new_command.args)


    @staticmethod
    def show_filter(task_filter=None):
        """
        Filtering user's tasks according to desired filter
        :param task_filter:
        :return:
        """
        try:
            with open(JSON_DATABASE_PATH, "r") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return

        if not task_filter:
            data_to_show = [task for task in data["tasks"] if data["tasks"]["status"] == task_filter]
        else:
            data_to_show = data["tasks"]

    @staticmethod
    def status_change(command: Command) -> None:
        """
        Updating status of task
        :param command:
        :return:
        """
        new_status = command.command.split("-", 1)[1]
        task_id, = command.args
        try:
            with open(JSON_DATABASE_PATH, "r") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return

        for tasks in data["tasks"]:
            if tasks["task_id"] == int(task_id):
                tasks["status"] = new_status
                tasks["updated_at"] = datetime.now().isoformat()

        with open(JSON_DATABASE_PATH, "w") as f:
            json.dump(data, f, indent=4)


    @staticmethod
    def update_task(command: list) -> None:
        """
        Name change of task
        :param command:
        :return:
        """
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
        """
        Add task to DB
        :param task_desc:
        :return:
        """
        file_path = get_path("../..", "database", "json_database.json")
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
        """
        Delete task from DB
        :param task_id:
        :return:
        """
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


