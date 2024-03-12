from aiogram.filters import BaseFilter
from aiogram.types import Message
from aiogram.filters import CommandObject

from typing import Any, List

class CheckForDigit(BaseFilter):

    async def __call__(self, message: Message, command: CommandObject) -> bool:
        command: CommandObject = command
        arg = command.args

        if arg.isnumeric() or (arg.count('.') == 1 and arg.replace('.','').isnumeric()):
            return True 
        return False



