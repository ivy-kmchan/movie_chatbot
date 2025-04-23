import chromadb
from chromadb.config import Settings
from typing import List, Dict
import json

class MovieVectorStore:
    def __init__(self):
        self.client = chromadb.PersistentClient(path="movie_db")
        self.collection = self.client.get_or_create_collection(
            name="movies",
            metadata={"hnsw:space": "cosine"}
        )

    def add_movie(self, movie_data: Dict):
        """Add a movie to the vector store"""
        # Convert movie data to string for embedding
        movie_text = json.dumps(movie_data)
        
        self.collection.add(
            documents=[movie_text],
            metadatas=[movie_data],
            ids=[movie_data['imdbID']]
        )

    def search_movies(self, query: str, n_results: int = 5) -> List[Dict]:
        """Search for movies in the vector store"""
        results = self.collection.query(
            query_texts=[query],
            n_results=n_results
        )
        
        if results['metadatas']:
            return results['metadatas'][0]
        return []

    def get_movie_by_id(self, movie_id: str) -> Dict:
        """Get a movie by its IMDb ID"""
        results = self.collection.get(ids=[movie_id])
        if results['metadatas']:
            return results['metadatas'][0]
        return None
