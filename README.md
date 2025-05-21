# Python Reference Search

A command-line tool for searching Python code patterns, methods, and reference snippets using fuzzy search and a rich terminal UI.

## Usage

Run the search tool:

```
python search.py
```

You will be prompted to enter a search query. Results will be shown with code examples and explanations.

## Customizing the Knowledge Base

You can add, edit, or remove reference entries by modifying the JSON file:

```
new_reference/python_reference.json
```

This file contains all the code snippets, explanations, and categories used by the search tool.

---

- Requires Python 3.7+
- Dependencies: `fuzzywuzzy`, `rich`
- Install dependencies:

```
pip install -r requirements.txt
```

---

Feel free to expand the knowledge base or adjust the search logic as needed!
