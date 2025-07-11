# 🧠 TrendScout

TrendScout is a simple Flask application that surfaces trending Google queries and tags them with intent keywords. It can optionally provide AI generated suggestions using OpenAI.

## Features
- Fetch trending Google search data by keyword and region
- Basic scoring and intent tagging
- Optional GPT suggestions

## Installation
```bash
# Clone the repository
git clone https://github.com/sandiren/TrendScout.git
cd TrendScout

# Install dependencies
pip install -r requirements.txt

# Download the spaCy model
python -m spacy download en_core_web_sm
```

Create a `.env` file if you want to enable GPT suggestions:
```ini
OPENAI_API_KEY=your_api_key
```

## Usage
Run the application with:
```bash
python app.py
```
Then open `http://127.0.0.1:5000` in your browser and search for a keyword.

## License
MIT License — free for personal and commercial use with attribution.
