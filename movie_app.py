import statistics
import random

class MovieApp:
    def __init__(self, storage):
        """initialize new storage. Storage should be StorageJson or StorageCsv object"""
        self._storage = storage

    def _command_list_movies(self):
        """uses print_movie_list of the storage/prints all the movies saved in the file """
        self._storage.print_movie_list()


    def _movies_rating_only(self):
        """From the self._movies of the object creates smaller dictionary self._movies_rating {name: rating}"""
        self._movies_rating = {}
        for k, v in self._storage._movies_list:
            self._movies_rating[k] = float(v['rating'])
        return self._movies_rating

    def _command_movie_stats(self):
        """From the self._movies of the object creates smaller dictionary self._movies_rating {name: rating}
        and calculates stats. This is for easier stats execution"""
        self._movies_rating = self._movies_rating_only()
        average_raiting = round(statistics.mean(self._movies_rating.values()), 2)
        highest_rating = max(self._movies_rating.values())
        highest_name = max(self._movies_rating, key=self._movies_rating.get)
        worst_rating = min(self._movies_rating.values())
        worst_name = min(self._movies_rating, key=self._movies_rating.get)
        median_rating = round(statistics.median(self._movies_rating.values()), 2)
        print(f'Average raiting: {average_raiting}')
        print(f'Median rating: {median_rating}')
        print(f'Best movie: {highest_name} : {highest_rating}')
        print(f'Worst movie: {worst_name} : {worst_rating}')

    def _generate_website(self):
        """Generates a web page using index_template.html. The user chooses between sorting the movies by year or by rating.
        Notes added to img title only if they exist"""
        page_name = input("Enter your movie app name ")
        user_sort = input("To sort by year press 1, to sort by rating press 2 ")
        html_sourse = ""
        while True:
            if user_sort != "1" and user_sort != "2":
                print("Wrong selection")
            if user_sort == "1":
                sorted_movies = sorted(self._storage._movies.items(), key=lambda x: x[1]['year'])
            elif user_sort == "2":
                sorted_movies = sorted(self._storage._movies.items(), key=lambda x: -float(x[1]['rating']))
            break
        for item in sorted_movies:
            html_sourse += f'<li> \n ' \
                           f'\t<div class="movie"> \n ' \
                           f'\t\t<a href="https://www.imdb.com/title/{item[1]["imdbID"]}/" target="_blank">\n\t\t\t\t<div class="container"> \n' \
                           f'\t\t\t\t<img class="movie-poster" src="{item[1]["img"]}" title="'
            if 'notes' in item[1]:
                html_sourse += f'{item[1]["notes"]}. '
            html_sourse += f'Open IMDB for full info">\n' \
                           f'<div class="overlay">{item[1]["rating"]}</div></div></a>' \
                           f'<div class="movie-title">{item[0]}</div>' \
                           f'\t\t<div class="movie-year">{item[1]["year"]}</div> \n' \
                           f'\t</div> \n' \
                           f'</li>\n'
        with open("index_template.html", "r") as handle:
            htmldata = handle.read()
        htmldata = htmldata.replace("__TEMPLATE_MOVIE_GRID__", html_sourse)
        htmldata = htmldata.replace("__TEMPLATE_TITLE__", page_name)
        new_html_name = self._storage.path.split(".")[0] + ".html"
        with open(new_html_name, 'w') as file:
            file.write(htmldata)
        print(f"Web page {new_html_name} was created")

    def _random_movie(self):
        """Prints random movie from _storage._movies"""
        random_movie = random.choice(list(self._storage._movies.keys()))
        print(f"Your movie for tonight: {random_movie}: {self._storage._movies[random_movie]['rating']}")

    def _search_movie(self):
        """Search movie by word or part of it in movies"""
        search = input("Enter part of movie name: ")
        # found is a new list of pairs key, value that contains only pairs where key in lower case contains search in lower case
        found = [(k, v) for k, v in self._storage._movies_list if search.lower() in k.lower()]
        if len(found) == 0:
            print("Not found. Please try again")
            return
        else:
            for item in found:
                print(item[0], item[1]['rating'])

    def _movies_by_rating(self):
        """Prints the list of movies by rating, using self method _movies_rating_only"""
        self._movies_rating = self._movies_rating_only()
        self._sorted_movies = sorted(self._movies_rating.items(), key=lambda x: -x[1])
        for name, rating in self._sorted_movies:
            print(name, rating)

    def run(self):
        """Main function using dictionary of commands to call function by number"""
        dict_fun = {}
        dict_fun[1] = self._command_list_movies
        dict_fun[2] = self._storage.add_movie
        dict_fun[3] = self._storage.delete_movie
        dict_fun[4] = self._storage.update_movie
        dict_fun[5] = self._command_movie_stats
        dict_fun[6] = self._generate_website
        dict_fun[7] = self._random_movie
        dict_fun[8] = self._search_movie
        dict_fun[9] = self._movies_by_rating
        while True:
            print("""
                ********** My Movies Database **********
                 Menu:
                0. Exit
                1. List movies
                2. Add movie
                3. Delete movie
                4. Add notes
                5. Stats
                6. Generate website
                7. Random movie
                8. Search
                9. Movies by rating (print)
            """
                  )
            option = int(input("Enter choice (0-9):  "))
            if 1 == option or 5 <= option <= 9:
                dict_fun[option]()
                input("Press enter to continue")
            elif 2 <= option <= 3:
                title = input("Title: ")
                dict_fun[option](title)
            elif option == 4:
                title = input("Title: ")
                notes = input("Notes: ")
                dict_fun[option](title, notes)
            else:
                print("Bye!")
                break