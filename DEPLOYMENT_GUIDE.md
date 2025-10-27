# Deployment Guide

This guide will help you deploy your Movie Chatbot to **Streamlit Cloud** (recommended) and **Vercel** (alternative).

## Table of Contents
- [Streamlit Cloud Deployment](#streamlit-cloud-deployment) (Recommended)
- [Vercel Deployment](#vercel-deployment) (Alternative)
- [Troubleshooting](#troubleshooting)

---

# Streamlit Cloud Deployment

This is the **recommended** deployment method as the app is built with Streamlit.

## Prerequisites

- GitHub account
- Streamlit Cloud account (sign up at https://streamlit.io/cloud)
- OpenAI API key
- OMDb API key

## Step 1: Push Your Code to GitHub

1. **Initialize Git repository** (if not already done):
```bash
git init
git add .
git commit -m "Initial commit"
```

2. **Create a new repository** on GitHub
3. **Push your code**:
```bash
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

**Important:** Make sure `.gitignore` is in place to avoid committing:
- `.env` file
- `.streamlit/secrets.toml`
- `__pycache__/`
- `movie_db/`
- `venv-py311/`

## Step 2: Deploy to Streamlit Cloud

1. **Go to** [share.streamlit.io](https://share.streamlit.io)
2. **Sign in** with your GitHub account
3. **Click "New app"**
4. **Configure your app**:
   - Repository: Select your repository
   - Branch: `main`
   - Main file path: `chatbot.py`
5. **Click "Deploy"**

## Step 3: Configure Secrets in Streamlit Cloud

After deploying your app to Streamlit Cloud, you need to add your API keys as secrets:

1. **Go to your app dashboard** in Streamlit Cloud
2. **Click on your app** to open its settings
3. **Navigate to the "Settings" menu** (three dots or gear icon)
4. **Select "Secrets"**
5. **Paste the following configuration** (replace with your actual API keys):

```toml
[openai]
api_key = "sk-your-actual-openai-api-key"

[omdb]
api_key = "your-actual-omdb-api-key"
```

6. **Click "Save"**
7. **Reboot your app** if it doesn't automatically restart

## Step 4: Local Testing with Secrets

To test locally using the same secrets format:

1. Create a file `.streamlit/secrets.toml` in your project root
2. Copy the content from `.streamlit/secrets.toml.example`
3. Replace the placeholder values with your actual API keys
4. Run your app: `streamlit run chatbot.py`

**Important:** Make sure `.streamlit/secrets.toml` is in your `.gitignore` to avoid committing secrets!

## Step 5: Verify Deployment

After adding secrets:

1. Your app should automatically reboot
2. Test the chatbot by asking movie questions
3. Check the logs for any errors

## Troubleshooting

### Error: "st.secrets has no key 'openai'"

This means secrets are not configured. Follow Step 1 above to add them.

### Error: "OpenAI API key is invalid"

- Double-check your OpenAI API key in the secrets
- Ensure there are no extra spaces or quotes
- Verify the key is active in your OpenAI account

### Error: "OMDb API key is invalid"

- Verify your OMDb API key at http://www.omdbapi.com/
- Ensure you've activated the key via email
- Check for any typos in the secrets configuration

### App crashes or doesn't load

- Check the app logs in Streamlit Cloud dashboard
- Verify all dependencies in `requirements.txt` are correct
- Ensure the ChromaDB database directory is being created properly

## Notes

- The app will automatically fall back to environment variables (`.env` file) when running locally if secrets are not found
- For production, always use Streamlit Cloud secrets instead of environment variables
- Never commit your `.env` or `.streamlit/secrets.toml` files to version control

## Getting API Keys

### OpenAI API Key
1. Go to https://platform.openai.com/
2. Sign up or log in
3. Navigate to API keys section
4. Create a new secret key
5. Copy and save it immediately (you won't see it again)

### OMDb API Key
1. Go to http://www.omdbapi.com/apikey.aspx
2. Choose the free tier (1,000 requests/day)
3. Enter your email
4. Check your email for the activation link
5. Activate your key
6. Copy your API key from the email

---

# Vercel Deployment

⚠️ **Important Note:** Streamlit apps are not natively supported on Vercel. Vercel is designed for Next.js, React, and other web frameworks. However, you have two options:

## Option 1: Keep Using Streamlit Cloud (Recommended)

Streamlit Cloud is **free**, **optimized** for Streamlit apps, and **easier** to deploy. This is the best option for your current app.

## Option 2: Convert to a Vercel-Compatible Architecture

If you need to deploy on Vercel, you'll need to restructure your app:

### Architecture for Vercel:
1. **Backend API** (FastAPI or Flask) - Hosts the movie chatbot logic
2. **Frontend** (Next.js/React) - User interface
3. **Deploy Backend** - On Vercel or Railway/Render
4. **Deploy Frontend** - On Vercel

### Quick Start: Create a FastAPI Backend

I can help you create a FastAPI version of this app that works with Vercel. Here's what you'd need:

#### Step 1: Create `api/main.py` for Vercel

```python
# This would be a FastAPI backend that Vercel can deploy
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/chat")
async def chat(message: str):
    # Your chatbot logic here
    pass
```

#### Step 2: Create `vercel.json`

```json
{
  "builds": [
    {
      "src": "api/main.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "api/main.py"
    }
  ]
}
```

#### Step 3: Update Dependencies

Create `requirements.txt` for the API:
```
fastapi
uvicorn
langchain
langchain-openai
openai
requests
chromadb
```

### Environment Variables for Vercel

1. Go to your Vercel project settings
2. Navigate to "Environment Variables"
3. Add:
   - `OPENAI_API_KEY` = your OpenAI key
   - `OMDB_API_KEY` = your OMDb key

### Would You Like Me to Convert Your App?

If you really need Vercel deployment, I can:
1. Create a FastAPI backend API
2. Create a simple Next.js frontend
3. Set up proper Vercel configuration

**But I strongly recommend sticking with Streamlit Cloud** for simplicity and better performance for this type of app.

---

## Comparison: Streamlit Cloud vs Vercel

| Feature | Streamlit Cloud | Vercel |
|---------|----------------|--------|
| **Setup Time** | 5 minutes | 1-2 hours (requires conversion) |
| **Cost** | Free | Free (with limits) |
| **Difficulty** | Easy | Moderate-Hard |
| **Best For** | Data apps, dashboards | Web apps, APIs |
| **Your App** | ✅ Native support | ❌ Requires conversion |

