from typing import Tuple
from uuid import uuid4, UUID

# from src.cli.validator import Validator


class Command(object):

    def __init__(self, command, args):
        self._command: str = command
        self._id: UUID = uuid4()
        self._args: Tuple[str, int] = args
        # self._validator = Validator()

    def __str__(self):
        return f"Command {self._command} with args {self._args} | ID: {self._id}"

    # async def validate(self) -> bool:
    #     if not self._validator.validate(self._command, self._args):
    #         pass



