from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="Salesforce/codegen-350M-mono"
)

def generate_comment(code: str) -> str:
    prompt = f"Add clear Python comments and docstrings to the following code:\n{code}\n"
    result = generator(prompt, max_length=200, do_sample=True)
    return result[0]["generated_text"]
