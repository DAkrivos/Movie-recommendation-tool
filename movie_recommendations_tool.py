# Import the spaCy library for NLP
import spacy

# Load en_core_web_md
nlp = spacy.load('en_core_web_md')

# Create function which takes in movie description as a parameter and returns title of most similar movie.
def recommend_next_movie(description):

  # Read contents of movie list file
  with open("movies.txt", "r") as movies:
    # Split each movie entry into title and description
    movie_list = [line.strip().split('<=>') for line in movies]

  # Get the number of movies in the list
  num_movies = len(movie_list)

  # Create a list to store similarity scores
  similarity_scores = []

  # Represent the description as a spaCy document
  model_sentence = nlp(description)

  # Iterate through each movie in the list
  for i in range(num_movies):
    # Represent the movie description as a spaCy document
    movie_description = nlp(movie_list[i][1])

    # Calculate the similarity score between the descriptions
    similarity_scores.append(model_sentence.similarity(movie_description))

  # Find the index of the movie with the highest similarity score
  most_similar_index = similarity_scores.index(max(similarity_scores))

  # Return the title of the most similar movie
  return movie_list[most_similar_index][0]

# Movie description to compare with
planet_hulk_description = """Will he save their world or destroy it? 
When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. 
Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."""

# Call function to recommend next similar movie and print movie title
print("If you liked this movie, you might also like:", recommend_next_movie(planet_hulk_description))
