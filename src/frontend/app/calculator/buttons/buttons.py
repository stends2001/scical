from dataclasses import dataclass
from typing import List, Iterator, Optional, Literal, Dict, Any

from .appearance import input_button_appearance, system_button_appearance, warning_button_appearance, notimplemented_button_appearance, ans_button_appearance

ButtonType = Literal['input','system','notimplemented', 'ans']

@dataclass 
class Button:
    """
    Simple Button-dataclass with
    """
    label:              str
    type:               ButtonType
    _value:             Optional[str] = None     
    _representation:    Optional[str] = None
    _span:              Optional[int] = None               
    col:                Optional[int] = None       

    @property 
    def span(self) -> int:
        if self._span:
            return self._span 
        return 1

    @property 
    def value(self) -> str:
        if self._value:
            return self._value
        else:
            return self.label

    @property 
    def representation(self) -> str:
        if self._representation:
            return self._representation
        else:
            return self.label
    
    @property
    def appearance(self) -> Dict[str, Any]:
        if self.type == 'input':
            return input_button_appearance
        elif self.type == 'system' and self.value in ['clear','del','backspace']:
            return warning_button_appearance
        elif self.type == 'system':
            return system_button_appearance
        elif self.type == 'ans':
            return ans_button_appearance        
        elif self.type == 'notimplemented':
            return notimplemented_button_appearance
        else:
            raise ValueError(f'no appearance for this type of button {self.type}')

@dataclass 
class ButtonGrid:
    """
    simple grid of Buttons with 

    Parameters
    ----------
    buttons: List[List[Button]]
        a list of rows of buttons
    nrow: int
        number of rows
    ncol: int
        number of columns

    Methods
    ------
    `__iter__()` loops through the entire list (returns rows of buttons)
    """

    buttons: List[List[Button]]
    nrow:    int 
    ncol:    int 

    def __post_init__(self):
        if self.nrow != len(self.buttons):
            raise ValueError('nrows != number of rows in buttons')

        if self.ncol != len(self.buttons[0]):
            raise ValueError('ncols != number of cols in buttons')

    def __iter__(self) -> Iterator[List[Button]]:
        return iter(self.buttons)