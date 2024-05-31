import pickle
import os

class Loader:
    initialized: bool = False
    base_path: str = ""
    data_resources: dict = {}
    file_associations: dict = {}

    @classmethod
    def get_full_path(cls, path: str):
        return os.path.join(cls.base_path, path)

    @staticmethod
    def load_pickle(path: str):
        with open(path, 'rb') as file:
            return pickle.load(file)
        
    def get_import_file_path(file_path: str):
        return os.path.basename(file_path) + "_import.pkl"

    @classmethod
    def load(cls, path: str, managed: bool = True) -> object:
        extension = os.path.splitext(path)[1]
        if extension in cls.file_associations:
            full_path: str = cls.get_full_path(path)
            cls.data_resources[full_path] = getattr(cls, cls.file_associations[extension])(full_path)
            return cls.data_resources[full_path]
        else:
            raise ValueError(f"Extension {extension} not supported. To add support, add a new method to the file_associations.pkl resource.")
        
    @classmethod
    def initialize(cls):
        cls.file_associations = cls.load_pickle(cls.get_full_path(".engine_resources/file_associations.pkl"))
        cls.initialized = True

Loader.initialize()