import threading

from src.cli.tasks.task import Task
from asyncio import run

class TaskManager:

    def __init__(self, i_queue):
        self.q = i_queue
        self._running = True
        threading.Thread(target=self.run).start()

    def run(self) -> None:
        while self._running:
            data = self.q.get()
            print(f"got {data}")
            # TODO: ADD DATA VALIDATION
            new_task = Task(data[0], data[1])
            print(new_task)
            # await self.response()

    def stop(self) -> None:
        self._running = False

    # async def response(self) -> None:
    #     raise NotImplementedError



