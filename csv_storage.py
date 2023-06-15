from istorage import IStorage
import shutil


class StorageCsv(IStorage):
    """class of parent IStorage, based on csv file. Class creates internal dictionary self._movies based on csv file"""
    def __init__(self, file_path):
        """create new csv storage-object with unique file path for this storage
        ***
        Please note: as comma might be used in movie title - csv file is based on ';' separator
        __init__ creates self._movies dict for internal use. Same as StorageJson
        All the changes added to this dict and the csv file updated
        """
        self.path = file_path
        with open(self.path, "r") as handle:
            self.csv_data_lines = handle.readlines()
        self._movies = {}
        for line in self.csv_data_lines[2:]:
            if any(field.strip() for field in line):
                title, rating, year, img, imdbID, notes = line.strip().split(";")
                self._movies[title] = {}
                self._movies[title]['rating'] = rating
                self._movies[title]['year'] = year
                self._movies[title]['img'] = img
                self._movies[title]['imdbID'] = imdbID
                self._movies[title]['notes'] = notes
        self._movies_list = self._movies.items()

    def update_file(self):
        """this function is called after each time changes should be added/saved in the json file"""
        with open('temp.csv', "w") as temp:
            temp.write('sep=";"\n')
            temp.write('title;rating;year;img;imdbID;notes\n')
            for k, v in self._movies_list:
                title = k
                rating = v['rating']
                year = v['year']
                img = v['img']
                imdbID = v['imdbID']
                notes = v['notes']
                temp.write(f"{title};{rating};{year};{img};{imdbID};{notes}\n")
        shutil.copyfile('temp.csv', self.path)
