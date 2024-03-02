# Function to recommend movies based on a target genre
def recommend_movie_by_genre(target_genre):
    movie_list = []
    with open("movies.txt", "r") as movies:
        # Split each line into title, genres, and description
        movie_list = [line.strip().split('<=>') for line in movies if line.strip()]
    
    # Initialise a list to hold titles of movies that match the target genre
    genre_matched_movies = []

    # Check each movie to see if the target genre is in its genre list
    for title, genres, _ in movie_list:
        if target_genre.lower() in genres.lower().split(','):
            genre_matched_movies.append(title)
    
    # Return the list of movies that match the genre
    return genre_matched_movies

# Example: looking for Action movies
target_genre = "Action"
recommended_movies = recommend_movie_by_genre(target_genre)
print(f"If you like {target_genre} movies, you might also like:")
for movie in recommended_movies:
    print(movie)

