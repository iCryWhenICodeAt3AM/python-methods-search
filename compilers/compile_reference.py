import json
import re
import os

def parse_docstring_block(block):
    """Parse a triple-quoted docstring block into a structured section."""
    # Remove leading/trailing whitespace and triple quotes
    block = block.strip().strip('"')
    lines = [line.strip() for line in block.split('\n') if line.strip()]
    if not lines:
        return None
    # The first non-empty line is the section title
    title = lines[0]
    purpose = ""
    syntax = ""
    examples = []
    example_lines = []
    in_example = False
    for line in lines[1:]:
        if line.startswith('Purpose:'):
            purpose = line[len('Purpose:'):].strip()
        elif line.startswith('How to use:'):
            syntax = line[len('How to use:'):].strip()
        elif line.startswith('Sample usage:'):
            in_example = True
        elif in_example:
            if line == '':
                if example_lines:
                    examples.append('\n'.join(example_lines))
                    example_lines = []
            else:
                example_lines.append(line)
    if example_lines:
        examples.append('\n'.join(example_lines))
    return {
        "title": title,
        "purpose": purpose,
        "syntax": syntax,
        "examples": examples
    }

def compile_reference(input_files, output_file):
    """Compile the reference guide from multiple text files to JSON."""
    reference = {
        "title": "Python Reference Guide",
        "categories": {}
    }
    for input_file in input_files:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        category_name = os.path.splitext(os.path.basename(input_file))[0].replace('python_', '').replace('_', ' ').title()
        # Find all triple-quoted blocks
        blocks = re.findall(r'"""(.*?)"""', content, re.DOTALL)
        sections = []
        for block in blocks:
            section = parse_docstring_block(block)
            if section:
                sections.append(section)
        reference["categories"][category_name] = sections
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(reference, f, indent=2, ensure_ascii=False)

def search_reference(json_file, query):
    """Search the reference guide for a specific query."""
    with open(json_file, 'r', encoding='utf-8') as f:
        reference = json.load(f)
    results = []
    for cat, sections in reference.get('categories', {}).items():
        for section in sections:
            for key in ['title', 'purpose', 'syntax']:
                if query.lower() in section.get(key, '').lower():
                    results.append({
                        "category": cat,
                        "section": section.get('title', ''),
                        "field": key,
                        "match": section.get(key, '')
                    })
            for example in section.get('examples', []):
                if query.lower() in example.lower():
                    results.append({
                        "category": cat,
                        "section": section.get('title', ''),
                        "field": 'example',
                        "match": example
                    })
    return results

if __name__ == "__main__":
    input_files = [
        "Info/python_data_manipulations.py",
        "Info/python_list_operations.py",
        "Info/python_methods_reference.py",
        "Info/python_number_conversions.py",
        "Info/python_string_manipulations.py"
    ]
    compile_reference(input_files, "python_reference.json")
    query = "list comprehension"
    results = search_reference("python_reference.json", query)
    print(f"\nSearch results for '{query}':")
    for result in results:
        print(f"\nCategory: {result['category']}")
        print(f"Section: {result['section']}")
        print(f"Field: {result['field']}")
        print(f"Match: {result['match'][:100]}...")