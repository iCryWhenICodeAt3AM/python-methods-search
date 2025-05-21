import json

sections = []
with open('compiled.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

in_section = False
current = []
for line in lines:
    if line.strip().startswith('"""'):
        if in_section:
            # End of section
            if current:
                # Find title
                non_empty = [l for l in current if l.strip()]
                title = non_empty[0].strip() if non_empty else "Untitled"
                content = ''.join(current).strip()
                sections.append({
                    "title": title,
                    "content": content,
                    "file": "compiled.txt"
                })
            current = []
            in_section = False
        else:
            in_section = True
            current = []
    elif in_section:
        current.append(line)

with open('compiled_manual.json', 'w', encoding='utf-8') as f:
    json.dump(sections, f, indent=2, ensure_ascii=False)

print(f"Extracted {len(sections)} sections to compiled_manual.json")