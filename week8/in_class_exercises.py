# P1
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def start(self):
        print(f"The {self.year} {self.make} {self.model} is starting.")
    
    def stop(self):
        print(f"The {self.year} {self.make} {self.model} is stopping.")

# Example usage:
my_car = Car("Toyota", "Camry", 2022)
my_car.start()
my_car.stop()

# P2
class Vehicle:
    def __init__(self, make, year):
        self.make = make
        self.year = year
    
    def display_info(self):
        print(f"This is a {self.year} {self.make} vehicle.")

class Car(Vehicle):
    def __init__(self, make, year, model):
        super().__init__(make, year)
        self.model = model
    
    def display_info(self):
        super().display_info()
        print(f"It is a {self.model}.")

# Example usage:
my_car = Car("Toyota", 2022, "Camry")
my_car.display_info()

#P3
class Movie:
    def __init__(self, title, release_year, rating):
        self.title = title
        self.release_year = release_year
        self.rating = rating
    
    def display_info(self):
        print(f"Title: {self.title}, Year: {self.release_year}, Rating: {self.rating}")

class TVShow(Movie):
    def __init__(self, title, release_year, rating, seasons):
        super().__init__(title, release_year, rating)
        self.seasons = seasons
    
    def display_info(self):
        super().display_info()
        print(f"Number of Seasons: {self.seasons}")

# Example usage:
movie = Movie("The Matrix", 1999, 8.7)
movie.display_info()

tv_show = TVShow("Breaking Bad", 2008, 9.5, 5)
tv_show.display_info()

#P4
class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration
    
    def display_info(self):
        print(f"Song: {self.title}, Artist: {self.artist}, Duration: {self.duration} minutes")

class Podcast(Song):
    def __init__(self, title, artist, duration, host, episodes):
        super().__init__(title, artist, duration)
        self.host = host
        self.episodes = episodes
    
    def display_info(self):
        super().display_info()
        print(f"Hosted by: {self.host}, Episodes: {self.episodes}")

# Example usage:
song = Song("Yesterday", "The Beatles", 2.5)
song.display_info()

podcast = Podcast("Tech Talk", "Tech Media", 45.0, "John Smith", 100)
podcast.display_info()