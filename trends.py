from pytrends.request import TrendReq
import pandas as pd
import re
import spacy

# Load English NLP model
nlp = spacy.load("en_core_web_sm")

# Define intent-related keyword tags
TAGS = {
    'vs': r'\bvs\b|\bversus\b',
    'best': r'\bbest\b',
    'cheap': r'\bcheap\b',
    'near_me': r'\bnear me\b|\bclose to\b',
    'buy': r'\bbuy\b|\border\b',
}

# Remove irrelevant or distracting queries
BLACKLIST = {'facebook', 'youtube', 'porn', 'instagram', 'netflix', 'news', 'weather'}

# Assign score based on trend value and tags
def score_query(query, value, is_rising):
    base_score = value if value else 0
    trend_boost = 20 if is_rising else 0
    intent_bonus = sum(10 for tag, pattern in TAGS.items() if re.search(pattern, query, re.IGNORECASE))
    return base_score + trend_boost + intent_bonus

# Extract intent tags from a query
def extract_tags(query):
    return [tag for tag, pattern in TAGS.items() if re.search(pattern, query, re.IGNORECASE)]

# NLP filter: only allow queries with nouns/proper nouns
def nlp_filter(query):
    doc = nlp(query.lower())
    return any(token.pos_ in {'NOUN', 'PROPN'} for token in doc)

# Main function to get trends and score them
def get_trends(keyword, region, timeframe='today 12-m'):
    if not keyword or not region:
        raise ValueError("Keyword and region must be non-empty.")

    pytrends = TrendReq(hl='en-US', tz=360)

    try:
        pytrends.build_payload([keyword], geo=region, timeframe=timeframe)
    except Exception as e:
        print("⚠️ build_payload error:", e)
        raise ValueError("❌ Google Trends rejected the keyword or region. Try something else.")

    try:
        related = pytrends.related_queries().get(keyword, {})
        print("🔍 Related Queries Fetched:", related)
    except Exception as e:
        print("⚠️ related_queries error:", e)
        raise ValueError("❌ Failed to fetch related trends. Please try again.")

    top = related.get('top')
    rising = related.get('rising')

    def process_df(df, is_rising=False):
        if df is None or df.empty or 'query' not in df.columns or 'value' not in df.columns:
            return []

        df = df[~df['query'].isin(BLACKLIST)]
        df = df[df['query'].apply(nlp_filter)]
        df['tags'] = df['query'].apply(extract_tags)
        df['score'] = df.apply(lambda row: score_query(row['query'], row['value'], is_rising), axis=1)
        df['source'] = 'rising' if is_rising else 'top'
        df['gpt'] = "💡 GPT suggestion disabled"
        return df.sort_values(by='score', ascending=False).to_dict(orient='records')

    results = process_df(top, is_rising=False) + process_df(rising, is_rising=True)

    if not results:
        raise ValueError("⚠️ No usable trends found for this keyword/region.")

    return results