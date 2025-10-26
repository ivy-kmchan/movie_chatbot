# Movie Chatbot

A conversational AI chatbot that answers questions about movies using the OMDb API, vector database storage, and GraphQL.

## Features

- Movie information retrieval using OMDb API
- Vector-based search using ChromaDB
- GraphQL API for structured queries
- Conversational interface using Streamlit
- RAG (Retrieval-Augmented Generation) for accurate responses

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure environment variables:
Create a `.env` file with:
```
OMDB_API_KEY=your_omdb_api_key
OPENAI_API_KEY=your_openai_api_key
```

3. Run the chatbot:
```bash
streamlit run chatbot.py
```

## Usage

1. The chatbot will start on http://localhost:8501
2. Type your movie-related questions in the chat input
3. The system will search for relevant movie information and provide detailed answers

## Components

- `movie_api.py`: Handles OMDb API interactions
- `vector_store.py`: Manages the ChromaDB vector database
- `graphql_schema.py`: Defines the GraphQL schema and resolvers
- `chatbot.py`: Implements the Streamlit chat interface

## Deployment

### Streamlit Cloud

1. Push your code to GitHub
2. Connect your repository to Streamlit Cloud
3. Configure secrets in the Streamlit Cloud dashboard (see `DEPLOYMENT_GUIDE.md`)
4. Deploy!

For detailed deployment instructions, see [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md).
