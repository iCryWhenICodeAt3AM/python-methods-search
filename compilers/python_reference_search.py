"""
Python Reference Search Helper
============================

This file provides functions to search through Python reference files
and find specific concepts, examples, or usage patterns.
"""

import os
import re

def search_reference_files(query, file_pattern="python_*.py"):
    """
    Search through Python reference files for specific concepts or examples.
    
    Args:
        query (str): Search query (e.g., "how to create list", "list comprehension")
        file_pattern (str): Pattern to match reference files
        
    Returns:
        list: List of tuples containing (file_name, section_title, content)
    """
    results = []
    
    # Get all reference files
    reference_files = [f for f in os.listdir('.') if f.startswith('python_') and f.endswith('.py')]
    
    for file_name in reference_files:
        with open(file_name, 'r', encoding='utf-8') as file:
            content = file.read()
            
            # Find all sections (text between triple quotes)
            sections = re.finditer(r'"""(.*?)"""', content, re.DOTALL)
            
            for section in sections:
                section_text = section.group(1)
                
                # Check if query matches section
                if query.lower() in section_text.lower():
                    # Extract section title
                    title_match = re.search(r'^([^\n-]+)', section_text.strip())
                    title = title_match.group(1).strip() if title_match else "Untitled Section"
                    
                    results.append((file_name, title, section_text.strip()))
    
    return results

def print_search_results(results):
    """Print search results in a formatted way."""
    if not results:
        print("No results found.")
        return
    
    for i, (file_name, title, content) in enumerate(results, 1):
        print(f"\n{'='*80}")
        print(f"Result {i}:")
        print(f"File: {file_name}")
        print(f"Section: {title}")
        print(f"{'-'*80}")
        print(content)
        print(f"{'='*80}\n")

def main():
    """Interactive search interface."""
    print("Python Reference Search")
    print("=====================")
    print("Enter your search query (e.g., 'how to create list', 'list comprehension')")
    print("Type 'exit' to quit")
    
    while True:
        query = input("\nSearch query: ").strip()
        
        if query.lower() == 'exit':
            break
            
        if not query:
            print("Please enter a search query.")
            continue
            
        results = search_reference_files(query)
        print_search_results(results)

if __name__ == "__main__":
    main() 