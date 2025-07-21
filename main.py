from src.predict import predict_sentiment

nepali_text = "सेयर बजारमा आज तीव्र गिरावट आएको छ।"
predicted_sentiment = predict_sentiment(nepali_text)

print(f"Nepali Input: {nepali_text}")
print(f"Predicted Sentiment: {predicted_sentiment}")
