# main.py
import mood_ai
import counselor

print("=== 🎧 Mood-Jukebox (exit: q) ===")

while True:
    txt = input("\nHow are you feeling right now? (English): ")
    if txt == 'q': break
    
    try:

        emo, score = mood_ai.analyze_emotion(txt)
        
        percentage = score * 100
        
        print(f"👉 Emotion detected: {emo} (Confidence: {percentage:.1f}%)")
        
        rec = counselor.recommend_song(emo)
        print(rec)
        
    except Exception as e:
        print(f"Error: {e}")