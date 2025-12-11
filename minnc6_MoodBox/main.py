# main.py
import mood_ai
import counselor

print("=== 🎧 Mood-Jukebox (종료: q) ===")

while True:
    txt = input("\n기분이 어떠신가요? (영어): ")
    if txt == 'q': break
    
    try:

        emo, score = mood_ai.analyze_emotion(txt)
        
        percentage = score * 100
        
        print(f"👉 분석 결과: {emo} (확신도: {percentage:.1f}%)")
        
        rec = counselor.recommend_song(emo)
        print(rec)
        
    except Exception as e:
        print(f"에러: {e}")