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
