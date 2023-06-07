from movie_app import MovieApp
from json_storage import StorageJson
from csv_storage import StorageCsv

storage_json = StorageJson("david_movies.json")
storage_csv = StorageCsv('ana_movies.csv')

def main():
    """Launches run() from movie_app.py, user selects file to work with"""
    user_format = ""
    while True:
        user_format = input(" Enter 'csv' or 'json' ")
        if user_format == "json" or user_format == "csv":
            break
    if user_format == "csv":
        print("Please note: use separator ';' in csv file, not comma")
        movie_app = MovieApp(storage_csv)
    elif user_format == "json":
        movie_app = MovieApp(storage_json)
    movie_app.run()


if __name__ == "__main__":
    main()
