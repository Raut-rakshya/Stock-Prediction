from transformers import pipeline
import torch

class FinBERTSentiment:
    def __init__(self):
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        print(f"Device set to use {device}")
        self.pipe = pipeline(
            "text-classification",
            model="ProsusAI/finbert",
            return_all_scores=True,
            device=0 if torch.cuda.is_available() else -1
        )

    def predict(self, text):
        outputs = self.pipe(text)
        if isinstance(outputs, list) and len(outputs) > 0:
            scores = outputs[0]
            sorted_scores = sorted(scores, key=lambda x: x['score'], reverse=True)
            label = sorted_scores[0]['label']
            return label.capitalize()
        return "Neutral"
