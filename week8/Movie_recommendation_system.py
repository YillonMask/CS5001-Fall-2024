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

class MovieRecommendationSystem:
    def __init__(self):
        self.content_list = []
        self.genre_dict = {}
    
    def add_movie_or_tv_show(self, content, genre):
        self.content_list.append(content)
        
        if genre not in self.genre_dict:
            self.genre_dict[genre] = []
        self.genre_dict[genre].append((content,genre))
    
    def search_by_title(self, title):
        for content in self.content_list:
            if content.title.lower() == title.lower():
                content.display_info()
                return
        print(f"No content found with title: {title}")
    
    def get_recommendations_by_genre(self, genre):
        if genre not in self.genre_dict:
            print(f"No content found in genre: {genre}")
            return
        
        sorted_content = sorted(self.genre_dict[genre], 
                              key=lambda x: x.rating, 
                              reverse=True)
        
        print(f"\nTop 3 recommendations in {genre}:")
        for content in sorted_content[:3]:
            content.display_info()
    
    def display_all(self):
        print("\nAll content in the system:")
        for content in self.content_list:
            content.display_info()
            print()

# Example usage:
def main():
    # Create recommendation system
    rs = MovieRecommendationSystem()
    
    # Add some movies
    movie1 = Movie("The Dark Knight", 2008, 9.0)
    movie2 = Movie("Inception", 2010, 8.8)
    movie3 = Movie("Interstellar", 2014, 8.6)
    
    # Add some TV shows
    tv1 = TVShow("Breaking Bad", 2008, 9.5, 5)
    tv2 = TVShow("Game of Thrones", 2011, 9.3, 8)
    
    # Add content to the system with genres
    rs.add_movie_or_tv_show(movie1, "Action")
    rs.add_movie_or_tv_show(movie2, "Sci-Fi")
    rs.add_movie_or_tv_show(movie3, "Sci-Fi")
    rs.add_movie_or_tv_show(tv1, "Drama")
    rs.add_movie_or_tv_show(tv2, "Drama")
    
    # Test the functionality
    print("Searching for a specific title:")
    rs.search_by_title("Inception")
    
    print("\nGetting recommendations for Sci-Fi genre:")
    rs.get_recommendations_by_genre("Sci-Fi")
    
    print("\nGetting recommendations for Drama genre:")
    rs.get_recommendations_by_genre("Drama")
    
    # Display all content
    rs.display_all()

if __name__ == "__main__":
    main()