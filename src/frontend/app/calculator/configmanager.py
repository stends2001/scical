import tkinter as tk
from typing import TYPE_CHECKING, Dict, Any
import yaml 

if TYPE_CHECKING:
    from ...backend import PathManager

class ConfigManagerMixin:
    """
    Calculator Mixin-class Config - manager
    loads config file and sets attributes
    """

    root:           tk.Tk
    pathmanager:    'PathManager'

    def set_config(self):
        config              = self._load_config()

        for attr_name, attr_value in config.items():
            self.__setattr__(attr_name, attr_value)

    def _load_config(self) -> Dict[str, Any]:
        filepath = self.pathmanager.config
        with open(filepath, "r") as f:
            return yaml.safe_load(f)        
        
        