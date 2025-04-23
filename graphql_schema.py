import graphene
from movie_api import OMDbAPI
from vector_store import MovieVectorStore

class Movie(graphene.ObjectType):
    title = graphene.String()
    year = graphene.String()
    rated = graphene.String()
    released = graphene.String()
    runtime = graphene.String()
    genre = graphene.String()
    director = graphene.String()
    writer = graphene.String()
    actors = graphene.String()
    plot = graphene.String()
    imdb_id = graphene.String()
    imdb_rating = graphene.String()

class Query(graphene.ObjectType):
    movie_by_title = graphene.Field(Movie, title=graphene.String(required=True))
    search_movies = graphene.List(Movie, query=graphene.String(required=True))
    
    def resolve_movie_by_title(self, info, title):
        api = OMDbAPI()
        movie_data = api.search_movie(title)
        if movie_data:
            return Movie(
                title=movie_data.get('Title'),
                year=movie_data.get('Year'),
                rated=movie_data.get('Rated'),
                released=movie_data.get('Released'),
                runtime=movie_data.get('Runtime'),
                genre=movie_data.get('Genre'),
                director=movie_data.get('Director'),
                writer=movie_data.get('Writer'),
                actors=movie_data.get('Actors'),
                plot=movie_data.get('Plot'),
                imdb_id=movie_data.get('imdbID'),
                imdb_rating=movie_data.get('imdbRating')
            )
        return None

    def resolve_search_movies(self, info, query):
        vector_store = MovieVectorStore()
        movies = vector_store.search_movies(query)
        return [
            Movie(
                title=movie.get('Title'),
                year=movie.get('Year'),
                rated=movie.get('Rated'),
                released=movie.get('Released'),
                runtime=movie.get('Runtime'),
                genre=movie.get('Genre'),
                director=movie.get('Director'),
                writer=movie.get('Writer'),
                actors=movie.get('Actors'),
                plot=movie.get('Plot'),
                imdb_id=movie.get('imdbID'),
                imdb_rating=movie.get('imdbRating')
            )
            for movie in movies
        ]

schema = graphene.Schema(query=Query)
