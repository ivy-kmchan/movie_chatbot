import streamlit as st
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from movie_api import OMDbAPI
from vector_store import MovieVectorStore
from graphql_schema import schema

load_dotenv()

# Get API keys from Streamlit secrets (cloud) or environment variables (local)
try:
    openai_api_key = st.secrets["openai"]["api_key"]
    omdb_api_key = st.secrets["omdb"]["api_key"]
except (KeyError, FileNotFoundError):
    openai_api_key = os.getenv("OPENAI_API_KEY")
    omdb_api_key = os.getenv("OMDB_API_KEY")

# Validate API keys
if not openai_api_key:
    st.error("⚠️ OpenAI API key is missing! Please configure it in Streamlit Cloud secrets.")
    st.stop()

if not omdb_api_key:
    st.warning("⚠️ OMDb API key is missing. Some features may not work.")

# Set OpenAI API key in environment for langchain
os.environ["OPENAI_API_KEY"] = openai_api_key

# Initialize components
movie_api = OMDbAPI(api_key=omdb_api_key)
vector_store = MovieVectorStore()

# Initialize ChatOpenAI with try-except to show better error messages
try:
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.7
    )
except Exception as e:
    st.error(f"❌ Error initializing ChatOpenAI: {str(e)}")
    st.error(f"API Key starts with: {openai_api_key[:10]}..." if openai_api_key else "API Key is None")
    st.stop()






def initialize_session_state():
    if 'messages' not in st.session_state:
        st.session_state.messages = []

def process_movie_query(user_input: str):
    # Create a system message for the chatbot
    system_msg = SystemMessage(content="""
    You are a helpful movie expert chatbot. Use the provided movie information to answer questions.
    Format your responses in a conversational way. If you don't have enough information,
    kindly ask for clarification.
    If you do not know the answer, simply say you do not know.
    """)
    
    # Search for relevant movies in the vector store
    movies = vector_store.search_movies(user_input)
    
    # Create context from movie data
    context = "Based on the following movies: "
    for movie in movies:
        context += f"{movie['Title']} ({movie['Year']}): {movie['Plot']}. "
    
    # Combine user input with context
    human_msg = HumanMessage(content=f"Context: {context}\nQuestion: {user_input}")
    
    # Get response from LLM
    response = llm([system_msg, human_msg])
    return response.content

def main():
    st.title("🎬 Movie Chatbot")
    st.write("Ask me anything about movies!")
    
    initialize_session_state()
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    
    # Chat input
    if user_input := st.chat_input("Ask about movies..."):
        # Display user message
        with st.chat_message("user"):
            st.write(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Get and display assistant response
        with st.chat_message("assistant"):
            response = process_movie_query(user_input)
            st.write(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()
