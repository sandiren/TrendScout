# 🧠 TrendScout

**TrendScout** is a Python-based web app that helps you discover trending keywords and identify niche opportunities using Google Trends and AI-powered keyword suggestion. It’s designed for entrepreneurs, content creators, and digital marketers looking to uncover hot topics, market gaps, or viral product ideas.

---

## 🚀 Features

- 🔍 Fetch trending Google search data by keyword or region  
- 🤖 AI-powered keyword suggestions and bundling  
- 🧠 NLP tagging (e.g., "vs", "best", "cheap", "near me")  
- 📈 Trend score and scoring logic for idea evaluation  
- 📦 Export keyword data for analysis or use in campaigns  
- ⚡ Clean Flask app with responsive HTML front-end

---

## 🛠 Technologies Used

- Python 3.x  
- Flask  
- pandas  
- pytrends  
- spaCy (NLP)  
- HTML/CSS (Bootstrap or custom)

---

## 🧩 Project Structure

<pre>
TrendScout/
├── app.py               # Main Flask app
├── trends.py            # Google Trends + NLP logic
├── suggestions.py       # AI-powered keyword suggestions
├── templates/
│   └── index.html       # Front-end form and results display
├── static/
│   └── style.css        # Optional custom styles
├── .env                 # Environment variables (NOT pushed to GitHub)
├── .gitignore           # Ignores .env, __pycache__, etc.
└── README.md            # You are here
</pre>

---

## 🔧 Installation

1. **Clone the repo:**
   ```bash
   git clone https://github.com/sandiren/TrendScout.git
   cd TrendScout
(Optional) Create a virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Create a .env file (if needed):

ini
Copy
Edit
FLASK_APP=app.py
FLASK_ENV=development
API_KEY=your_api_key_here
Run the app:

bash
Copy
Edit
python app.py
🌐 How to Use
Open the app in your browser (usually http://127.0.0.1:5000)

Enter a seed keyword (e.g. toys, healthy snacks)

Choose a region (e.g. US, GB, IN)

Submit and view:

Trending queries

AI-generated suggestions

Intent-based tags (e.g., "vs", "cheap")

📌 TODOs
 Export results to CSV or Excel

 Add BERT-based topic clustering

 Add explainability for trend scoring

 Deploy to Render or Heroku

🔐 Security Note
Make sure .env is in .gitignore

Never push API keys or secrets to GitHub

If .env was committed, revoke and rotate the keys immediately

📜 License
MIT License — free for personal and commercial use with attribution.

