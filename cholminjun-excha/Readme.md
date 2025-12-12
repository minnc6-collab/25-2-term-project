# ✍️ 한국어 텍스트 문체 변환기 (Korean Style Transfer Tool)

## 1. Project Overview

본 프로젝트는 Hugging Face의 파인튜닝된 **KoBART Transformer 모델**을 사용하여 사용자 입력 텍스트를 원하는 스타일로 변환하는 오픈소스 SW입니다.

* **개발자:** 최민준 (GitHub ID: cholminjun_11)
* **주요 기능:** 입력된 텍스트를 '딱딱한', '친근한', '아재' 등 다양한 말투로 변환합니다.
* **핵심 기술:** Huggingface Transformers, KoBART 기반 Seq2Seq 모델.

---

## 2. Using package (사용한 패키지 및 그 version)

이 프로젝트는 다음 라이브러리를 사용합니다.

| Package | Purpose | Version (예시) |
| :--- | :--- | :--- |
| **transformers** | Hugging Face 모델 로드 및 사용 | 4.30.0+ |
| **torch** | 모델 실행을 위한 딥러닝 프레임워크 | 2.0.0+ |
| **pandas** | 데이터 처리 (선택) | 2.0.0+ |

---

## 3. Installation & Usage (실행 방법)

### Step 1: Install Packages

`requirements.txt` 파일을 사용하여 필요한 라이브러리를 설치합니다.

```bash
pip install -r requirements.txt

### Step 2: Run the program

'''bash
python main.py

4. Usage Example (데모 및 예시)
성공적으로 변환이 완료된 결과 화면입니다. 이는 코드가 올바르게 실행됨을 보여주는 데모입니다.

원문 (딱딱): "본 프로젝트는 기한 내에 완료되어야 하며, 모든 팀원은 지침을 엄수해야 합니다."

변환 (친근): "이 프로젝트는 정해진 시간 안에 끝내야 해요. 모두가 규칙을 잘 지켜야 합니다!"

<img width="1260" alt="Korean Style Transfer Demo" src="./model.png" />

## References
Hugging Face Model (파인튜닝된 문체 변환 모델): heegyu/kobart-text-style-transfer

KoBART 모델 기본 구조 및 Tokenizer: gogamza/kobart-base-v1

Hugging Face Transformers Pipeline Documentation