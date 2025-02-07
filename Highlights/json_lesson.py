# JSON = Javascript Object Notation

# Widely Used in APIs: Most modern web services and APIs use JSON as the default format for data exchange.
# Universal way of sharing data

#Best Practices for Writing JSON:
# Use Indentation: Always use the indent parameter to make JSON files readable.
# Ensure Data Types are JSON-Compatible:
# Python objects like dictionaries and lists map directly to JSON objects and arrays.
# Handle Errors Gracefully: Use try-except blocks to catch serialization errors.

import json

# Movie rating dictionary
movie_ratings = {
  'The Shawshank Redemption': 9.3,
  "The Godfather": 9.2,
  "The Dark Knight": 9.0,
  "Pulp Fiction": 8.9,
  "The Lord of the Rings: The Return of the King": 8.9,
  "Forrest Gump": 8.8,
  "Inception": 8.8,
  "Fight Club": 8.8,
}


# Serialize this dict to Json string
json_string = json.dumps(movie_ratings)
print(json_string)
print(type(json_string))

# Writing to json file
with open("movie_ratings.json", 'w') as file:
  json.dump(movie_ratings, file, indent=4)


# Deserialization

json_string = '{"name": "Maria", "age": 34, "city": "Malaga"}'

# convert this JSON string to Python dict
python_data = json.loads(json_string)

print(type(python_data))

print(python_data['name'])

# Read JSON Data
with open("movie_ratings.json", "r") as file:
  movies = json.load(file)

  print(movies)


