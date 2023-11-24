# Movie App

## Introduction
This Python project is a simple movie database application that allows users to manage their movie collection. The application supports adding, deleting, and updating movies, viewing statistics, generating a website, and more.

## Project Structure
The project consists of the following files:

1. **main.py**: The main entry point of the application. It initializes the storage type (JSON or CSV) based on user input and launches the MovieApp.

2. **StorageJson.py**: Implements the StorageJson class, a child of the IStorage class. It uses a JSON file as the storage backend and handles reading, updating, and writing movie data.

3. **StorageCsv.py**: Implements the StorageCsv class, another child of the IStorage class. It uses a CSV file as the storage backend and handles reading, updating, and writing movie data.

4. **istorage.py**: Defines the IStorage class, a parent class for different storage types. It contains common methods for managing movies.

5. **index_template.html**: A template HTML file used for generating a movie website. It includes placeholders for the movie grid and title.

6. **movie_app.py**: Implements the MovieApp class, which contains the main logic of the movie application. It interacts with the chosen storage backend and provides functionality such as listing movies, adding, deleting, and updating movies, generating statistics, and more.

7. **style.css**: A CSS file for styling the generated movie website.

## How to Use
1. **File Format Selection**: Run the `main.py` file to start the application. Choose between JSON and CSV as the file format for movie storage.

2. **Movie Management**: Use the menu options to list movies, add new movies, delete movies, add notes, view statistics, generate a website, and perform other operations.

3. **Statistics**: The application provides statistics such as average rating, median rating, best and worst movies, and more.

4. **Website Generation**: Generate a movie website with clickable movie posters that link to IMDb. Choose to sort the movies by year or rating.

5. **Random Movie**: Get a suggestion for a random movie to watch.

6. **Search Movies**: Search for movies by entering a part of the movie name.

7. **Movies by Rating**: Print the list of movies sorted by rating.

## Dependencies
The project requires the `requests` library for interacting with the OMDB API.

Install the required library using the following command:
```bash
pip install requests
