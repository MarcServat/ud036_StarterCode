import fresh_tomatoes
import movie
import httplib
import json

movies = []

# Prepare api call to get a list of movies
conn = httplib.HTTPSConnection("api.themoviedb.org")
conn.request("GET", "/3/list/62897?api_key=181786faaaf5a64117addec2dfef8a63")
res = conn.getresponse()
data = res.read().decode("utf-8")
response = json.loads(data)


def process_response(response):
    # Process response for a list of movies
    for item in response["items"]:
        movie_id = str(item["id"])
        img = "https://image.tmdb.org/t/p/w185_and_h278_bestv2"\
              + item["poster_path"]
        # Call to the api for each movie
        youtube_key = get_trailer(movie_id)
        youtube_url = "https://www.youtube.com/watch?v="+youtube_key
        # Initialize new intance movie
        m = movie.Movie(item["original_title"], img, youtube_url)
        movies.append(m)


def get_trailer(id):
    # Prepare url
    path = "/3/movie/"+id+"/videos?api_key=181786faaaf5a64117addec2dfef8a63"
    conn.request("GET", path)
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    # Convert response to json
    res_trailer = json.loads(data)
    # Return the youtube key
    results = res_trailer["results"]
    return results[0]["key"]

# Get data from reponse
process_response(response)
# Send list of movies to a frontend layer
fresh_tomatoes.open_movies_page(movies)
