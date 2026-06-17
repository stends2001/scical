import os 
from pathlib import Path

class PathManager():

    """ 
    Attributes
    ----------
    - project_dir
    - config
    """

    def __init__(self):
        self.project_root = self._resolve_project_root()
        self.config       = os.path.join(self.project_root, 'config', 'config.yaml')
        
    def _resolve_project_root(self) -> str:
        current_path = Path(__file__).resolve()

        for parent in current_path.parents:
            if (parent / "pyproject.toml").exists():
                return str(parent)

        raise RuntimeError("Could not find project root (looking for pyproject.toml)")