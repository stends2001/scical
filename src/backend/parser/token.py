from typing import Literal
from dataclasses import dataclass

TokenTypes = Literal['numerical','operator','skip','constant','parenthL','parenthR', 'function']

@dataclass
class Token:
    type:   TokenTypes
    value:  str