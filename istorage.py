from abc import ABC, abstractmethod
import json
import requests


class IStorage(ABC):

    def print_movie_list(self):
        """List of movies in self.movies. Prints name, rating and year
        self.movies created only in __init__ method of Json or Csv object"""
        for k, v in self.movies.items():
            print(f"{k} : {v['rating']}, {v['year']} ")

    def add_movie(self, title):
        """Checks if the title exist in self.movies dict. If not - using the omdb API to get the data. If raiting
        is unvailible user enters it manually.
        At the end uses add_movie_to file method to add changes to the file, different for csv/json"""
        if title in self.movies:
            print(f"Movie {title} already exist!")
            return
        else:
            url = "http://www.omdbapi.com/?apikey=d6b7eb59&t="
            request = requests.post(url + title)
            api_data = request.json()
            if "Error" in api_data:
                print("Wrong title. Please try again")
                return
            new_movie = api_data['Title']
            self.movies[new_movie] = {}
            try:
                self.movies[new_movie]['rating'] = float(api_data['imdbRating'])
            except:
                self.movies[new_movie]['rating'] = float(
                    input(f"Please enter rating manually for {api_data['Title']} "))
            self.movies[new_movie]['year'] = api_data['Year']
            self.movies[new_movie]['img'] = api_data['Poster']
            self.movies[new_movie]['imdbID'] = api_data['imdbID']
            self.new_csv_data = str(api_data['Title']) + ";" + str(self.movies[new_movie]['rating']) + ";" + str(
                api_data['Year']) + ";" + str(api_data['Poster']) + ";" + str(api_data['imdbID']) + ";"
            self.add_movie_to_file()
            print(f'Moovie {api_data["Title"]} successfully added')

    def delete_movie(self, title):
        """Checks if the title exist in self.movies dict. If yes - deletes it from self.movies and then uses
        delete_movie_from_file method to remove it from the file
        At the end uses delete_movie_from_file method to add changes to the file, different for csv/json"""
        if title not in self.movies:
            print(f"Movie {title} not found!")
            return
        else:
            self.movies.pop(title)
            self.delete_movie_from_file(title)
        print(f'Movie {title} successfully deleted')

    def update_movie(self, title, notes_user):
        """Checks if the title exist in self.movies dict. If yes - deletes it from self.movies and then add notes as a
        string to self.movies['notes']
        At the end uses update_file_notes method to add changes to the file, different for csv/json"""
        if title not in self.movies:
            print(f"Movie {title} not found!")
            return
        else:
            if "notes" not in self.movies[title]:
                self.movies[title]['notes'] = ""
            self.movies[title]['notes'] += f"Note: {notes_user}. "
            self.update_file_notes(title_user=title, notes_user=notes_user)
            print(f"Note: '{notes_user}' added to {title}")
