import sys

from src.cli.tasks.task_manager import TaskManager

if __name__ == '__main__':

    args = sys.argv[1:]
    if not args:
        print("Please enter input")
        sys.exit(1)

    tm = TaskManager()
    tm.run(args)
