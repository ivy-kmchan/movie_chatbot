import os
import requests
from typing import Dict, Optional
from dotenv import load_dotenv

load_dotenv()

class OMDbAPI:
    def __init__(self):
        self.api_key = os.getenv('OMDB_API_KEY')
        self.base_url = 'http://www.omdbapi.com/'

    def search_movie(self, title: str) -> Optional[Dict]:
        """Search for a movie by title"""
        params = {
            'apikey': self.api_key,
            't': title,
            'type': 'movie',
            'r': 'json'
        }
        
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            if data.get('Response') == 'True':
                return data
        return None

    def get_movie_by_id(self, imdb_id: str) -> Optional[Dict]:
        """Get movie details by IMDb ID"""
        params = {
            'apikey': self.api_key,
            'i': imdb_id,
            'r': 'json'
        }
        
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            if data.get('Response') == 'True':
                return data
        return None

if __name__ == '__main__':
    # Test the API
    api = OMDbAPI()
    movie = api.search_movie('Inception')
    if movie:
        print(f"Found movie: {movie['Title']} ({movie['Year']})")
