import requests

class IStorage():
    """Parent class for different file-types storages. Child object creates internal dictionary self._movies, based on
    file type, Istorage operates based on this dictionary"""
    def print_movie_list(self):
        """Dict of movies in self._movies with rating only. Prints name, rating and year
        self._movies created only in __init__ method of Json or Csv object"""
        for k, v in self._movies.items():
            print(f"{k} : {v['rating']}, {v['year']} ")

    def add_movie(self, title):
        """Checks if the title exist in self._movies dict. If not - using the omdb API to get the data. If raiting
        is unvailible user enters it manually.
        At the end uses add_movie_to file method to add changes to the file, different for csv/json"""
        if title in self._movies:
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
            self._movies[new_movie] = {}
            try:
                self._movies[new_movie]['rating'] = float(api_data['imdbRating'])
            except:
                self._movies[new_movie]['rating'] = float(
                    input(f"Please enter rating manually for {api_data['Title']} "))
            self._movies[new_movie]['year'] = api_data['Year']
            self._movies[new_movie]['img'] = api_data['Poster']
            self._movies[new_movie]['imdbID'] = api_data['imdbID']
            self._movies[new_movie]['notes'] = ""
            self.update_file()
            print(f'Moovie {api_data["Title"]} successfully added')


    def delete_movie(self, title):
        """Checks if the title exist in self._movies dict. If yes - deletes it from self._movies and then uses
        delete_movie_from_file method to remove it from the file
        At the end uses delete_movie_from_file method to add changes to the file, different for csv/json"""
        if title not in self._movies:
            print(f"Movie {title} not found!")
            return
        else:
            self._movies.pop(title)
            self.update_file()
        print(f'Movie {title} successfully deleted')

    def update_movie(self, title, notes_user):
        """Checks if the title exist in self._movies dict. If yes - deletes it from self._movies and then add notes as a
        string to self._movies['notes']
        At the end uses update_file_notes method to add changes to the file, different for csv/json"""
        if title not in self._movies:
            print(f"Movie {title} not found!")
            return
        else:
            if "notes" not in self._movies[title]:
                self._movies[title]['notes'] = ""
            self._movies[title]['notes'] += f"Note: {notes_user}. "
            self.update_file()
            print(f"Note: '{notes_user}' added to {title}")
