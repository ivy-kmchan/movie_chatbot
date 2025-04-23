# Movies Chatbot - Technical Details

## System Architecture

The Movies Chatbot is built using a modular architecture that combines several key technologies to provide an intelligent movie information retrieval system.

### Core Components

1. **Movie API Interface (`movie_api.py`)**
   - Handles all interactions with the OMDb API
   - Manages API key authentication
   - Provides structured movie data retrieval

2. **Vector Storage System (`vector_store.py`)**
   - Implements ChromaDB for efficient vector storage
   - Enables semantic search capabilities
   - Stores and retrieves movie information embeddings

3. **GraphQL API Layer (`graphql_schema.py`)**
   - Defines the GraphQL schema for structured queries
   - Implements resolvers for data fetching
   - Provides a standardized API interface

4. **Chat Interface (`chatbot.py`)**
   - Built with Streamlit for web-based interaction
   - Implements the conversational UI
   - Handles user input processing and response generation

## Technology Stack

### Core Dependencies
- Python 3.x
- Streamlit 1.31.1 (Web Interface)
- ChromaDB 0.4.22 (Vector Database)
- Graphene 3.3.0 (GraphQL Framework)
- LangChain 0.1.0 (LLM Framework)
- OpenAI 1.12.0 (Language Model)

### Additional Libraries
- Requests 2.31.0 (HTTP Client)
- Python-dotenv 1.0.0 (Environment Management)
- Pydantic 2.6.1 (Data Validation)
- Typing-extensions 4.9.0 (Type Hints)

## Data Flow

1. **User Input → Chat Interface**
   - User submits a movie-related question
   - Input is processed by the chatbot interface

2. **Query Processing**
   - Natural language query is converted to structured format
   - Vector embeddings are generated for semantic search

3. **Data Retrieval**
   - Vector store is queried for relevant movie information
   - OMDb API is called for additional movie details
   - GraphQL resolvers combine and structure the data

4. **Response Generation**
   - Retrieved data is processed using RAG
   - Coherent response is generated using the language model
   - Response is formatted and displayed to the user

## Environment Configuration

Required environment variables:
```
OMDB_API_KEY=<your_omdb_api_key>
OPENAI_API_KEY=<your_openai_api_key>
```

## Running the Application

1. **Environment Setup**
   ```bash
   pip install -r requirements.txt
   ```

2. **Starting the Application**
   ```bash
   streamlit run chatbot.py
   ```

3. **Accessing the Interface**
   - Open web browser
   - Navigate to http://localhost:8501

## System Requirements

- Python 3.x
- Sufficient RAM for vector storage (minimum 4GB recommended)
- Internet connection for API access
- Modern web browser for interface
