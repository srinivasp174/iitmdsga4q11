from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

# Create FastAPI app
app = FastAPI()


# -----------------------------
# Request Schema
# -----------------------------
class SentencesRequest(BaseModel):
    sentences: List[str]


# -----------------------------
# Sentiment Analysis Function
# -----------------------------
def detect_sentiment(sentence: str) -> str:

    text = sentence.lower()

    happy_words = [
        "love", "great", "excellent", "good", "happy",
        "amazing", "fantastic", "awesome", "nice", "wonderful"
    ]

    sad_words = [
        "terrible", "bad", "sad", "hate", "awful",
        "horrible", "worst", "angry", "disappointed", "poor"
    ]

    for word in happy_words:
        if word in text:
            return "happy"

    for word in sad_words:
        if word in text:
            return "sad"

    return "neutral"


# -----------------------------
# API Endpoint
# -----------------------------
@app.post("/sentiment")
def sentiment_analysis(data: SentencesRequest):

    results = []

    for sentence in data.sentences:

        sentiment = detect_sentiment(sentence)

        results.append({
            "sentence": sentence,
            "sentiment": sentiment
        })

    return {"results": results}