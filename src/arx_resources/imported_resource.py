from typing import Type
from .loader import Loader
from .resource import Resource
from copy import copy




class Imported_Resource (Resource):
    def __init__(self, import_path: str, resource_path: str = None) -> None:
        if resource_path == None:
            no_extension = "".join(import_path.split(".")[:-1])
            resource_path = no_extension + ".pkl"
        super().__init__(resource_path)
        self.import_path = import_path
        self.imported_resource = Loader.load(import_path, False)

    def create_individual(self) -> Resource:
        raise NotImplementedError("Imported resources cannot be individualized, as they cannot be duplicated.")

    def __getstate__(self) -> object:
        parent = super().__getstate__()
        if isinstance(parent, dict):
            parent.imported_resource = self.import_path
            parent.pop("import_path", None)
        return parent
        
    def __setstate__(self, state: object) -> None:
        super().__setstate__(state)
        if isinstance(state, dict):
            self.import_path = copy(self.imported_resource)
            self.imported_resource = Loader.load(self.import_path, False)