from typing import Type
from copy import deepcopy
from .loader import Loader
import pickle

class Resource:
    def __init__(self, file_path: str) -> None:
        self.path = file_path
        self.upper_level_pickle = False

    def create_individual(self) -> Type["Resource"]:
        individual_copy = deepcopy(self)
        individual_copy.path = None
        return individual_copy
    
    def __getstate__(self) -> object: 
        if self.path == None or self.upper_level_pickle:
            dict_copy = self.__dict__.copy()
            dict_copy.pop("upper_level_pickle",None)
            return dict_copy
        else:
            return self.path
        
    def __setstate__(self, state: object) -> None:
        if isinstance(state, str):
            self.__dict__ = Loader.load(state).__dict__.copy()
        else:
            self.__dict__ = state

    def save_to_file(self) -> None:
        self.upper_level_pickle = True
        with open(self.path, "wb") as fp:
            pickle.dump(self, fp)
        self.upper_level_pickle = False