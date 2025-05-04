import shlex
import queue

from src.cli.tasks.task_manager import TaskManager

if __name__ == '__main__':
    q = queue.Queue()
    task_manager = TaskManager(q)

    while True:
        try:
            r = shlex.split(input(">"))
            q.put(r)
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not r:
            continue




