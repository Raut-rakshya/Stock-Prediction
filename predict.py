from src.translator import translate_nepali_to_english
from src.finbert_predict import FinBERTSentiment

# Initialize FinBERT only once for performance
finbert_model = FinBERTSentiment()

def predict_sentiment(nepali_news: str) -> str:
    """
    Input: Nepali news in string format
    Output: Sentiment — 'Positive', 'Neutral', or 'Negative'
    """
    try:
        # Translate Nepali ➔ English
        english_news = translate_nepali_to_english(nepali_news)
        print(f"Translated: {english_news}")

        # Predict sentiment using FinBERT
        sentiment = finbert_model.predict(english_news)

        return sentiment
    except Exception as e:
        print(f"Error during prediction: {e}")
        return "Error"
