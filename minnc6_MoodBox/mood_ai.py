# mood_ai.py
from transformers import pipeline

print("⏳ AI 모델을 불러오는 중입니다...")
emotion_classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=1)

def analyze_emotion(text):
    result = emotion_classifier(text)
    
    label = result[0][0]['label']
    score = result[0][0]['score']
    
    return label, score