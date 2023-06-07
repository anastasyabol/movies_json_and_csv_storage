from istorage import IStorage
import json
import requests


class StorageJson(IStorage):
    def __init__(self, file_path):
        """create new json storage-object with unique file path for this storage"""
        self.path = file_path
        with open(self.path, "r") as handle:
            self.movies = json.load(handle)
        self.movies_list = self.movies.items()

    def update_file(self):
        """this function is called after each time changes should be added/saved in the json file"""
        with open(self.path, "w") as handle:
            json.dump(self.movies, handle)

    def add_movie_to_file(self):
        """uses update file func after movie added to self.movies"""
        self.update_file()

    def delete_movie_from_file(self, title):
        """uses update file func after movie deleted self.movies, parameters not in use"""
        self.update_file()

    def update_file_notes(self, title_user, notes_user):
        """uses update file func after notes added to self.movies, parameters not in use"""
        self.update_file()
