from comment_generator import generate_comment

print("Enter Python code (end with empty line):")

lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

code = "\n".join(lines)
output = generate_comment(code)

print("\nGenerated Result:\n")
print(output)
