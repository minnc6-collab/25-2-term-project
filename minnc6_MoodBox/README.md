# Mood-Jukebox

## 1. 프로젝트 개요
사용자의 영어 일기를 AI(HuggingFace)로 분석하여, 현 상태에 맞는 **유튜브 플레이리스트**를 추천해 주는 프로그램입니다.
* 사용자가 기분을 입력하면 7가지 감정(Joy, Sadness 등) 중 하나로 분석합니다.
* 분석된 감정을 기반으로 유튜브에서 최적의 플레이리스트를 찾아 링크를 제공합니다.

## 2. 사용 패키지 및 버전
이 프로젝트는 아래 라이브러리가 필요합니다.
* **transformers**: 감정 분석 AI 모델
* **torch**: AI 모델 구동용 프레임워크
* **ytmusicapi**: 유튜브 뮤직 검색 및 링크 생성

## 3. 설치 및 실행 방법

### Step 1: 패키지 설치
```bash
pip install transformers torch ytmusicapi
```

### Step 2: 프로그램 실행
```bash
python main.py
```

### Step 3: 실행 예시
<img width="1275" height="393" alt="image" src="https://github.com/user-attachments/assets/929d3678-0886-4b66-a8ea-0430d54de20e" />

## 4. 참고 자료
- Hugging Face Model: j-hartmann/emotion-english-distilroberta-base  
- ytmusicapi Documentation
