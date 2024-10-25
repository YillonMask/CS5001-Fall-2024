# IMDb Movie Recommendation System

# Dictionary to hold movies, where the key is the movie title
# and the value is another dictionary with 'genres' and 'actors'
movie_db = {}

# Function to add a new movie
def add_movie(title, genres, actors):
    if title in movie_db:
        print(f"Movie '{title}' already exists.")
    else:
        movie_db[title] = {'genres': genres, 'actors': set(actors)}
        print(f"Movie '{title}' added successfully.")
    # 如何增加多个 generes 和 actors？？
# Function to update an existing movie (add a new genre or actor)
def update_movie(title, genre=None, actor=None):
    if title in movie_db:
        if genre:
            movie_db[title]['genres'].append(genre)
        if actor:
            movie_db[title]['actors'].add(actor)
        print(f"Movie '{title}' updated successfully.")
    else:
        print(f"Movie '{title}' not found.")

# Function to remove a movie by title
def remove_movie(title):
    if title in movie_db:
        del movie_db[title]
        print(f"Movie '{title}' removed successfully.")
    else:
        print(f"Movie '{title}' not found.")

# Function to display movie details by title
def display_movie(title):
    if title in movie_db:
        movie = movie_db[title]
        print(f"Title: {title}")
        print(f"Genres: {', '.join(movie['genres'])}")
        print(f"Actors: {', '.join(movie['actors'])}")
    else:
        print(f"Movie '{title}' not found.")

# Function to recommend movies based on a genre
def recommend_movies_by_genre(genre):
    print(f"Movies in the genre '{genre}':")
    found = False
    for title, details in movie_db.items():
        if genre in details['genres']:
            print(f"- {title}")
            found = True
    if not found:
        print(f"No movies found in the genre '{genre}'.")

# Function to display all movies in the database
def display_all_movies():
    if movie_db:
        print("All movies in the database:")
        for title, details in movie_db.items():
            print(f"Title: {title}, Genres: {', '.join(details['genres'])}, Actors: {', '.join(details['actors'])}")
    else:
        print("No movies in the database.")

# Main program loop
def main():
    while True:
        print("\n--- IMDb Movie Recommendation System ---")
        print("1. Add a new movie")
        print("2. Update an existing movie")
        print("3. Remove a movie")
        print("4. Display a movie's details")
        print("5. Recommend movies by genre")
        print("6. Display all movies")
        print("7. Exit")
        
        choice = input("Choose an option (1-7): ")
        
        if choice == '1':
            title = input("Enter movie title: ")
            genres = input("Enter genres (comma-separated): ").split(',')
            actors = input("Enter actors (comma-separated): ").split(',')
            add_movie(title.strip(), [genre.strip() for genre in genres], [actor.strip() for actor in actors])
        
        elif choice == '2':
            title = input("Enter movie title to update: ")
            genre = input("Enter new genre (or press Enter to skip): ").strip()
            actor = input("Enter new actor (or press Enter to skip): ").strip()
            update_movie(title.strip(), genre if genre else None, actor if actor else None)
        
        elif choice == '3':
            title = input("Enter movie title to remove: ")
            remove_movie(title.strip())
        
        elif choice == '4':
            title = input("Enter movie title to display: ")
            display_movie(title.strip())
        
        elif choice == '5':
            genre = input("Enter genre to recommend movies for: ")
            recommend_movies_by_genre(genre.strip())
        
        elif choice == '6':
            display_all_movies()
        
        elif choice == '7':
            print("Exiting the system. Goodbye!")
            break
        
        else:
            print("Invalid option. Please choose a number between 1 and 7.")

# Run the main program loop
main()