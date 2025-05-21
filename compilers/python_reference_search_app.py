"""
Python Reference Search Application
=================================

A console application that searches through compiled Python reference data
using fuzzy matching and provides rich formatted output.
"""

import json
import os
from pathlib import Path
from typing import List, Dict, Optional
from fuzzywuzzy import fuzz
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.prompt import Prompt
import typer
from typer import Typer

# Initialize Typer app and Rich console
app = Typer()
console = Console()

class ReferenceDatabase:
    """Manages the reference database and search operations."""
    
    def __init__(self, db_path: str = "reference_db.json"):
        self.db_path = db_path
        self.data = self._load_database()
    
    def _load_database(self) -> Dict:
        """Load the reference database from JSON file."""
        if os.path.exists(self.db_path):
            with open(self.db_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {"references": []}
    
    def _save_database(self):
        """Save the reference database to JSON file."""
        with open(self.db_path, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)
    
    def add_reference(self, title: str, content: str, category: str, tags: List[str]):
        """Add a new reference to the database."""
        reference = {
            "title": title,
            "content": content,
            "category": category,
            "tags": tags
        }
        self.data["references"].append(reference)
        self._save_database()
    
    def search(self, query: str, threshold: int = 60) -> List[Dict]:
        """
        Search the database using fuzzy matching.
        
        Args:
            query: Search query
            threshold: Minimum similarity score (0-100)
            
        Returns:
            List of matching references
        """
        results = []
        for ref in self.data["references"]:
            # Search in title, content, and tags
            title_score = fuzz.partial_ratio(query.lower(), ref["title"].lower())
            content_score = fuzz.partial_ratio(query.lower(), ref["content"].lower())
            tag_scores = [fuzz.partial_ratio(query.lower(), tag.lower()) for tag in ref["tags"]]
            
            # Get the highest score
            max_score = max(title_score, content_score, max(tag_scores) if tag_scores else 0)
            
            if max_score >= threshold:
                ref["score"] = max_score
                results.append(ref)
        
        # Sort by score
        return sorted(results, key=lambda x: x["score"], reverse=True)

def compile_references():
    """Compile all reference files into the database."""
    db = ReferenceDatabase()
    
    # Clear existing data
    db.data = {"references": []}
    
    # Find all Python reference files
    ref_files = Path(".").glob("python_*.py")
    
    for file_path in ref_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
            # Extract sections (text between triple quotes)
            sections = content.split('"""')
            
            for i in range(1, len(sections), 2):
                if i + 1 < len(sections):
                    section = sections[i].strip()
                    
                    # Extract title and content
                    lines = section.split('\n')
                    title = lines[0].strip()
                    
                    # Extract category from file name
                    category = file_path.stem.replace('python_', '').replace('_', ' ').title()
                    
                    # Generate tags from content
                    content_lower = section.lower()
                    tags = []
                    if "how to" in content_lower:
                        tags.append("how-to")
                    if "example" in content_lower:
                        tags.append("example")
                    if "purpose" in content_lower:
                        tags.append("purpose")
                    
                    # Add to database
                    db.add_reference(title, section, category, tags)
    
    console.print("[green]References compiled successfully![/green]")

@app.command()
def compile():
    """Compile all reference files into the searchable database."""
    compile_references()

@app.command()
def search(
    query: str = typer.Argument(..., help="Search query"),
    threshold: int = typer.Option(60, "--threshold", "-t", help="Minimum match threshold (0-100)")
):
    """Search the reference database."""
    db = ReferenceDatabase()
    results = db.search(query, threshold)
    
    if not results:
        console.print("[yellow]No results found.[/yellow]")
        return
    
    for i, result in enumerate(results, 1):
        # Print in reference file style
        console.print(f"\n{'='*80}", style="cyan")
        console.print(f"File: [bold]{result.get('file', 'unknown')}[/bold]")
        console.print(f"Section: [bold]{result['title']}[/bold]")
        console.print(f"{'-'*80}")
        console.print(result['content'])
        console.print(f"{'='*80}\n", style="cyan")

@app.command()
def interactive():
    """Start interactive search mode."""
    db = ReferenceDatabase()
    
    console.print("[bold blue]Python Reference Search[/bold blue]")
    console.print("Type 'exit' to quit, 'help' for help")
    
    while True:
        query = Prompt.ask("\nSearch query")
        
        if query.lower() == 'exit':
            break
        elif query.lower() == 'help':
            console.print("""
[bold]Available commands:[/bold]
- Type your search query to search
- 'exit' to quit
- 'help' to show this help
            """)
            continue
        
        results = db.search(query)
        
        if not results:
            console.print("[yellow]No results found.[/yellow]")
            continue
        
        for i, result in enumerate(results, 1):
            console.print(f"\n{'='*80}", style="cyan")
            console.print(f"File: [bold]{result.get('file', 'unknown')}[/bold]")
            console.print(f"Section: [bold]{result['title']}[/bold]")
            console.print(f"{'-'*80}")
            console.print(result['content'])
            console.print(f"{'='*80}\n", style="cyan")

if __name__ == "__main__":
    app() 