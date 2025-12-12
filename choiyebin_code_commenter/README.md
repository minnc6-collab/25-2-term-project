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

### Step 3: Usage Example

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
---

### References 섹션 

```md
---

## 4. References
- HuggingFace Model: Salesforce/codegen-350M-mono
- HuggingFace Transformers Documentation

