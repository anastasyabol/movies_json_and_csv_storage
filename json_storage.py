from istorage import IStorage
import json


class StorageJson(IStorage):
    """class of parent IStorage, based on json file. Class creates internal dictionary self._movies based on csv file"""
    def __init__(self, file_path):
        """create new json storage-object with unique file path for this storage"""
        self.path = file_path
        with open(self.path, "r") as handle:
            self._movies = json.load(handle)
        self._movies_list = self._movies.items()

    def update_file(self):
        """this function is called after each time changes should be added/saved in the json file"""
        with open(self.path, "w") as handle:
            json.dump(self._movies, handle)
