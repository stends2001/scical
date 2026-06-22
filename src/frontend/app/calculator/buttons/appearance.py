from typing import Dict, Any

BASE_BUTTON_APPEARANCE: Dict[str, Any] = {
    'bg'                    : "white",
    'fg'                    : "black",
    'activeforeground'      : "black",
    'highlightbackground'   : "black",
    'bd'                    : 2,
    'relief'                : "solid",
    'highlightthickness'    : 1,
}

def make_button(arguments: Dict[str, Any]) -> Dict[str, Any]:
    return {
        **BASE_BUTTON_APPEARANCE,
        **arguments
    }

input_button_appearance             = make_button({'activebackground': 'lightgrey'})
system_button_appearance            = make_button({'activebackground': 'darkgrey'})
warning_button_appearance           = make_button({'activebackground': "#E65252", 'bg': '#F7A8A8'})
notimplemented_button_appearance    = make_button({'activebackground': "#CA7CC6", 'bg': "#CA7CC6"})
ans_button_appearance               = make_button({'activebackground': "#37D664", 'bg': "#8FCD94"})