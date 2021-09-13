import inspect
import re
from enum import Enum
from typing import Optional

from .example import Example
from .parameter import Parameter
from .returns import Returns


class Sections(str, Enum):
    PARAMETERS = "Parameters"


class Docstring:
    def __init__(self):
        self._description: Optional[str] = None
        self._parameters: Optional[list[Parameter]] = []
        self._return: Optional[Returns] = None
        self._examples: Optional[Example] = None

    @classmethod
    def parse(cls, docstring: str) -> 'Docstring':
        docstring = inspect.cleandoc(docstring)
        for line in docstring:
            # If short form
            if re.match(r"\((.*?)\)", line):
                pass

        return cls()
