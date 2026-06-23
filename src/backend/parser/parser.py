from typing import Optional, Tuple, List
import re 
import math
from typing import Dict, Callable
from .token import TokenTypes, Token

supported_basic_operators   = ['/','*','-','+', '**']
supported_advanced_operators= ['sqrt','ln']
supported_decimal           = '.'
supported_math_numbers      = ['e', 'pi']

CONSTANTS: Dict[str, float] = {
    'e'     : math.e,
    'pi'    : math.pi
}

FUNCS: Dict[str, Callable[[float], float]] = {
    'ln'    : math.log,
    'sqrt'  : math.sqrt,
    'exp'   : math.exp,
    'asin'  : math.asin,
    'acos'  : math.acos,
    'atan'  : math.atan,
    'sin'   : math.sin,
    'cos'   : math.cos,
    'tan'   : math.tan,
    'fac'   : math.factorial, # type: ignore
    'abs'   : abs, # type: ignore
    'int'   : int
} 

# Each rule describes HOW to recognize a piece of the string
TOKEN_SPEC: List[Tuple[TokenTypes, str]] = [
    ("numerical",   r"\d+(\.\d+)?"),            # matches any number of digits possibly including decimals
    ("operator",   r"\*\*|[+\-*^/]"),           # matches **, +, \, -, *
    ('function',    r"ln|exp|sqrt|asin|acos|atan|sin|cos|tan|fac|abs|int"),    
    ("constant",    r"pi|e"),                   # matches constants: pi, e
    ("skip",        r"\s+"),                    # matches whitespace (we ignore it)
    ('parenthL',    r"\("),
    ('parenthR',    r"\)"),
]
regex = "|".join(f"(?P<{name}>{pattern})" for name, pattern in TOKEN_SPEC)


class InputParser:
    expression_str:         str 
    cursor_idx:             int

    def append_input(self, input: str):
        
        idx = self.cursor_idx

        self.expression_str = self.expression_str[:idx] + input + self.expression_str[idx:]
        self.update_cursor(len(input))

    @property
    def tokenized_expression(self)-> List[Token]:

        tokens: List[Token] = []  # final output list

        # scan through the string left → right
        for match in re.finditer(regex, self.expression_str):

            kind: TokenTypes = match.lastgroup      # type: ignore
            value            = match.group()        # the actual text that was matched

            # ignore whitespace
            if kind == "skip":
                continue

            # turn match into a Token object
            tokens.append(Token(kind, value))

        return tokens
    
    def update_cursor(self, step: Optional[int]) -> None:
        pass    