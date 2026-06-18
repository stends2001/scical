from typing import Optional
from ..parser import InputParser, CONSTANTS, FUNCS

class CalculatorBackEnd(InputParser):
    """
    """
    expression_str:         str
    last_input_is_number:   bool
    cursor_idx:             int

    def __init__(self):
        self.reset_memory()       

    def evaluate(self):
        tokens = self.tokenized_expression

        out = ""

        for t in tokens:

            match t.type:

                case "numerical":
                    out += t.value
                case "operator":
                    if t.value == "^":
                        out += "**"
                    else:
                        out += t.value
                case "constant":
                    out += str(CONSTANTS[t.value])
                case 'parenthL':
                    out += t.value 
                case "function":
                    out += f"FUNCS['{t.value}']"  
                    print(out)       
                case 'parenthR':
                    out += t.value
                case "skip":
                    continue 

        return eval(out, {"__builtins__": {}, 'FUNCS' : FUNCS}, {})
    
    def resolve_system_input(self, input: str):
        if input == ">":
            self.cursor_idx += 1
        elif input == "<":
            self.cursor_idx += -1
        elif input == 'clear':
            self.reset_memory()
        elif input == 'ans':
            self.ans()
        elif input == 'del':
            self.delete()
        elif input == 'backspace':
            self.backspace()

    def delete(self):
        
        idx = self.cursor_idx
        if idx < len(self.expression_str):
            self.expression_str = self.expression_str[:idx] + self.expression_str[idx+1:]
            self.update_cursor(0)

    def backspace(self):

        idx = self.cursor_idx

        if idx > 0:
            self.expression_str = (
                self.expression_str[:idx - 1] +
                self.expression_str[idx:]
            )
            self.update_cursor(-1)
            
    def ans(self):
        result                      = str(self.evaluate())
        self.expression_str         = result
        self.last_input_is_number   = True
        self.update_cursor()
        
    def reset_memory(self) -> None:
        """reset all attributes to initial state"""
        self.expression_str         = ''    
        self.last_input_is_number   = False
        self.cursor_idx             = 0

    def update_cursor(self, step: Optional[int] = None) -> None:
        if step is None:
            idx = len(self.expression_str)

        else:
            idx = self.cursor_idx + step 
            if idx < 0:
                idx = 0
            elif idx >= len(self.expression_str):
                idx = len(self.expression_str)
        
        self.cursor_idx = idx

    @property
    def is_evaluable(self)->bool:
        try:
            self.evaluate()
            return True
        except Exception:
            return False

    @property
    def result(self)->str:
        if self.is_evaluable:
            return str(self.evaluate())
        
        elif len(self.expression_str) == 0:
            return ''
        
        else:
            return 'NaN'

    @property
    def bracket_depth(self) -> tuple[int, int]:
        left = self.expression_str.count("(")
        right = self.expression_str.count(")")
        return (left, right)

    def get_display_expression(self, cursor: bool = False) -> str:
        if cursor:
            sep = "|"
        else:
            sep = " "

        expression = self.expression_str[:self.cursor_idx] + sep + self.expression_str[self.cursor_idx:] 
        return expression     

    def __repr__(self):
        representation = f'<{self.__class__.__name__}(expression: {self.expression_str}, result: {self.result})>'
        return representation