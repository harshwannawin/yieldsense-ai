# Streamlit Cloud Deployment Guide

## 🚀 Step-by-Step Deployment

### 1. Deploy to Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with your GitHub account
3. Click "New app"
4. Select:
   - **Repository:** `harshwannawin/yieldsense-ai`
   - **Branch:** `main`
   - **Main file path:** `app.py`

### 2. Configure Secrets (IMPORTANT!)

Before the app runs successfully, you need to add your API key:

1. In your app dashboard, click the "⚙️ Settings" button (bottom right)
2. Click on "Secrets" in the left menu
3. Add the following (replace with your actual key):

```toml
GROQ_API_KEY = "gsk_YOUR_ACTUAL_KEY_HERE"
```

4. Click "Save"
5. The app will automatically restart with the secret configured

### 3. Test Your App

- The API key input box is now hidden from users
- The app loads the key automatically from secrets
- Users can immediately start using the store!

## 🔐 Security Notes

- Never commit API keys to GitHub
- The `.streamlit/secrets.toml` file is ignored by git
- On Streamlit Cloud, secrets are encrypted and secure
- Each deployment environment has its own secrets

## 🆘 Troubleshooting

**Error: "groq library missing"**
- Solution: Already fixed in requirements.txt

**Error: Pricing returns None**
- Solution: Already handled with fallback pricing

**API key not working**
- Make sure you've added it in Streamlit Cloud Secrets
- Format must be: `GROQ_API_KEY = "your_key"`
- Check there are no extra spaces or quotes

## 📱 App URL

After deployment, Streamlit Cloud will give you a URL like:
`https://yieldsense-ai.streamlit.app`

Share this with users - they won't need any API keys!
