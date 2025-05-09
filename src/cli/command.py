from typing import Tuple


class Command(object):

    def __init__(self, command, args):
        self.command: str = command
        self.args: Tuple[str, int] = args
        # self._validator = Validator()

    def __str__(self):
        return f"Command {self.command} with args {self.args} "

    # async def validate(self) -> bool:
    #     if not self._validator.validate(self._command, self._args):
    #         pass



