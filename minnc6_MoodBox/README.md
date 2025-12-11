\# Mood-Jukebox



\## 1. Project Overview

This program analyzes your English diary using AI(HuggingFace) and recommends a \*\*YouTube playlist\*\* that fits your current mood.

\* When you input your feelings, the AI classifies them into one of 7 emotions (e.g., Joy, Sadness).

\* Based on the analyzed emotion, it searches for the perfect playlist on YouTube and provides the link.



\## 2. Using package

This project requires the following libraries:

\* \*\*transformers\*\*: AI model for emotion analysis

\* \*\*torch\*\*: Framework for running the AI model

\* \*\*ytmusicapi\*\*: Used to search YouTube Music and generate links



\## 3. Installation \& Usage



\### Step 1: Install Packages

```bash

pip install transformers torch ytmusicapi

```



\### Step 2: Run the program

```bash

python main.py

```



\### Step 3: Usage Example

<img width="1260" height="467" alt="image" src="https://github.com/user-attachments/assets/9e67eefe-dc25-4467-9113-77fe5ad223fd" />





\## 4. References

\- Hugging Face Model: j-hartmann/emotion-english-distilroberta-base  

\- ytmusicapi Documentation



