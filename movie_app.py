import statistics


class MovieApp:
    def __init__(self, storage):
        """initialize new storage. Storage should be StorageJson or StorageCsv object"""
        self._storage = storage

    def _command_list_movies(self):
        """uses print_movie_list of the storage/prints all the movies saved in the file """
        self._storage.print_movie_list()

    def _command_movie_stats(self):
        """From the self.movies of the object creates smaller dictionary self.movies_rating {name: rating}
        and calculates stats. This is for easier stats execution"""
        self.movies_rating = {}
        for k, v in self._storage.movies.items():
            self.movies_rating[k] = float(v['rating'])
        average_raiting = round(statistics.mean(self.movies_rating.values()), 2)
        highest_rating = max(self.movies_rating.values())
        highest_name = max(self.movies_rating, key=self.movies_rating.get)
        worst_rating = min(self.movies_rating.values())
        worst_name = min(self.movies_rating, key=self.movies_rating.get)
        median_rating = round(statistics.median(self.movies_rating.values()), 2)
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
                sorted_movies = sorted(self._storage.movies.items(), key=lambda x: x[1]['year'])
            elif user_sort == "2":
                sorted_movies = sorted(self._storage.movies.items(), key=lambda x: -float(x[1]['rating']))
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

    def run(self):
        """Main function using dictionary of commands to call function by number"""
        dict_fun = {}
        dict_fun[1] = self._command_list_movies
        dict_fun[2] = self._storage.add_movie
        dict_fun[3] = self._storage.delete_movie
        dict_fun[4] = self._storage.update_movie
        dict_fun[5] = self._command_movie_stats
        dict_fun[6] = self._generate_website
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
            """
                  )
            option = int(input("Enter choice (0-6):  "))
            if 1 == option or 5 <= option <= 6:
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