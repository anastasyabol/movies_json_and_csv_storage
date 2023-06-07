from istorage import IStorage
import csv
import shutil


class StorageCsv(IStorage):
    def __init__(self, file_path):
        """create new csv storage-object with unique file path for this storage
        ***
        Please note: as comma might be used in movie title - csv file is based on ';' separator
        __init__ creates self.movies dict for internal use. Same as StorageJson
        All the changes added to this dict and the csv file updated
        """
        self.path = file_path
        with open(self.path, "r") as handle:
            self.csv_data_lines = handle.readlines()
        self.movies = {}
        for line in self.csv_data_lines[2:]:
            if any(field.strip() for field in line):
                title, rating, year, img, imdbID, notes = line.strip().split(";")
                self.movies[title] = {}
                self.movies[title]['rating'] = rating
                self.movies[title]['year'] = year
                self.movies[title]['img'] = img
                self.movies[title]['imdbID'] = imdbID
                if notes != "":
                    self.movies[title]['notes'] = notes
        self.movies_list = self.movies.items()

    def add_movie_to_file(self):
        """Adds added movie as a new line to csv file"""
        with open(self.path, 'a', newline="") as handle:
            handle.write("\n" + self.new_csv_data)

    def delete_movie_from_file(self, title_user):
        """Loops through original csv file, copies all the movies except the one user deleted. Creates temp.csv file
        Continue to copy all the lines after not adding deleted one, then copies temp.csv to original csv path
        Skips blank rows in csv if they are exist"""
        with open(self.path, "r") as handle:
            self.csv_data_lines = handle.readlines()
        with open('temp.csv', "w") as temp:
            temp.write('sep=";"\n')
            temp.write('title;rating;year;img;imdbID;notes\n')
            for line in self.csv_data_lines[2:]:
                if any(field.strip() for field in line):
                    title, rating, year, img, imdbID, notes = line.strip().split(";")
                    if title != title_user:
                        temp.write(f"{title};{rating};{year};{img};{imdbID};{notes}\n")
        shutil.copyfile('temp.csv', self.path)

    def update_file_notes(self, title_user, notes_user):
        """Loops through original csv file, copies all the movies and adds notes_user if title_user matches title in csv
        Creates temp.csv file, then copies temp.csv to original csv path
        Skips blank rows in csv if they are exist"""
        with open(self.path, "r") as handle:
            self.csv_data_lines = handle.readlines()
        with open('temp.csv', "w") as temp:
            temp.write('sep=";"\n')
            temp.write('title;rating;year;img;imdbID;notes\n')
            for line in self.csv_data_lines[2:]:
                if any(field.strip() for field in line):
                    title, rating, year, img, imdbID, notes = line.strip().split(";")
                    if title != title_user:
                        temp.write(f"{title};{rating};{year};{img};{imdbID};{notes}\n")
                    else:
                        temp.write(f"{title};{rating};{year};{img};{imdbID};{notes}. {notes_user}\n")
        shutil.copyfile('temp.csv', self.path)
