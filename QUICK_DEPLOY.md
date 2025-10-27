# 🚀 Quick Deploy Guide

## Streamlit Cloud (5-Minute Deploy)

### Prerequisites
✅ GitHub account  
✅ OpenAI API key  
✅ OMDb API key  

### Steps

#### 1️⃣ Push to GitHub
```bash
# Make sure you have all the latest changes
git add .
git commit -m "Ready for deployment"
git push origin main
```

#### 2️⃣ Deploy to Streamlit Cloud
1. Go to **https://share.streamlit.io**
2. Click **"New app"**
3. Select your repository
4. Main file: `chatbot.py`
5. Click **"Deploy"**

#### 3️⃣ Add Secrets
1. Click the **⋮** menu on your app
2. Go to **Settings → Secrets**
3. Paste this (with your real keys):

```toml
[openai]
api_key = "sk-proj-your-key-here"

[omdb]
api_key = "your-omdb-key-here"
```

4. Click **"Save"**

#### 4️⃣ Done! 🎉
Your app will reboot and be live!

---

## Common Issues & Fixes

### ❌ "st.secrets has no key 'openai'"
**Fix:** You forgot to add secrets. Go back to Step 3.

### ❌ "Pydantic validation error"
**Fix:** Your API key might be wrong. Check:
- OpenAI key starts with `sk-` or `sk-proj-`
- No extra spaces in the secrets
- Keys are wrapped in quotes `"`

### ❌ "Module not found"
**Fix:** Make sure `requirements.txt` is in your repo and pushed to GitHub.

### ❌ App loads but chatbot doesn't respond
**Fix:** Check the logs:
1. Click **Manage app** (bottom right)
2. View the error logs
3. Usually an API key issue

---

## Test Locally Before Deploying

```bash
# 1. Add your secrets to .streamlit/secrets.toml
# (See .streamlit/secrets.toml.example)

# 2. Run the app
streamlit run chatbot.py

# 3. Test in your browser at http://localhost:8501
```

---

## Need Help?

- 📖 Full Guide: See `DEPLOYMENT_GUIDE.md`
- 🔑 Secrets Format: See `STREAMLIT_SECRETS_FORMAT.txt`
- 💬 Ask me anything!

