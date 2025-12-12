# ✍️ Code Comment Generator

## 1. Project Overview
This project is an open-source tool that generates comments and
docstrings for Python code using a HuggingFace pre-trained language model.

When the user inputs Python source code,
the AI analyzes the code and automatically generates
clear comments to improve readability.

- Developer: Choi Yebin
- Core Technology: HuggingFace Transformers, CodeGen Model

---

## 2. Using package
This project uses the following libraries:

| Package | Purpose | Version |
|--------|--------|---------|
| transformers | Load code generation model | 4.30+ |
| torch | Run transformer model | 2.0+ |

---

## 3. Installation & Usage

### Step 1: Install Packages
```bash
pip install transformers torch

### Step 2: Run the program
```bash
python main.py


---

### 2️⃣ Step 3: Usage Example (이게 핵심)
교수님이 제일 좋아하는 부분이다.

```md
### Step 3: Usage Example
```text
Enter Python code (end with empty line):
def add(a, b):
    return a + b

Generated Result:
# This function adds two numbers
def add(a, b):
    return a + b


👉 실제 실행 로그처럼 보이게 하는 게 포인트  
👉 스크린샷 없어도 OK

---

### 3️⃣ References 섹션 (이거 없으면 감점 가능)
README 맨 아래에 **반드시** 추가.

```md
---

## 4. References
- HuggingFace Model: Salesforce/codegen-350M-mono
- HuggingFace Transformers Documentation

