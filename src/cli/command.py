from typing import Tuple


class Command(object):

    def __init__(self, command, args):
        self.command: str = command
        self.args: Tuple[str, int] = args


    def __str__(self):
        return f"Command {self.command} with args {self.args} "
