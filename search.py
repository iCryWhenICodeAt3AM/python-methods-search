import json
from fuzzywuzzy import fuzz
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.syntax import Syntax
from rich.text import Text
from rich import box
from rich.prompt import Prompt
from rich.progress import Progress
import os
import re
from collections import defaultdict

class PythonReferenceSearch:
    def __init__(self, json_path):
        self.console = Console()
        self.json_path = json_path
        self.reference = self._load_reference()
        self.keyword_weights = {
            'list': 1.5,
            'string': 1.5,
            'dictionary': 1.5,
            'set': 1.5,
            'tuple': 1.5,
            'add': 1.3,
            'remove': 1.3,
            'find': 1.3,
            'search': 1.3,
            'convert': 1.3,
            'example': 0.8,
            'purpose': 1.2,
            'syntax': 1.2
        }
        
    def _load_reference(self):
        """Load the reference JSON file."""
        try:
            with open(self.json_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            self.console.print("[red]Error: Reference file not found![/]")
            return None
        except json.JSONDecodeError:
            self.console.print("[red]Error: Invalid JSON file![/]")
            return None

    def _calculate_keyword_score(self, text, query):
        """Calculate score based on keyword matches."""
        score = 0
        text_lower = text.lower()
        query_words = query.lower().split()
        
        for word in query_words:
            if word in self.keyword_weights:
                if word in text_lower:
                    score += self.keyword_weights[word]
                    
        return score

    def _extract_code_blocks(self, text):
        """Extract code blocks from text for syntax highlighting."""
        if not text:
            return []
            
        # Split the text into lines
        lines = text.split('\n')
        code_blocks = []
        current_block = []
        in_block = False
        
        for line in lines:
            # Check if line contains code (starts with # or contains = or other code indicators)
            is_code_line = (
                line.strip().startswith('#') or
                '=' in line or
                '(' in line or
                '[' in line or
                ']' in line or
                ':' in line or
                'def ' in line or
                'class ' in line or
                'import ' in line or
                'from ' in line or
                'return ' in line or
                'print(' in line or
                'if ' in line or
                'for ' in line or
                'while ' in line
            )
            
            if is_code_line:
                if not in_block and current_block:
                    code_blocks.append('\n'.join(current_block))
                    current_block = []
                in_block = True
                current_block.append(line)
            elif in_block and line.strip():
                current_block.append(line)
            elif in_block and not line.strip():
                if current_block:
                    code_blocks.append('\n'.join(current_block))
                    current_block = []
                in_block = False
                
        if current_block:
            code_blocks.append('\n'.join(current_block))
            
        # If no code blocks were found, treat the entire text as a code block
        if not code_blocks and text.strip():
            code_blocks = [text]
            
        return code_blocks

    def search(self, query, top_n=3):
        """Enhanced search with better matching algorithms."""
        if not self.reference:
            return []

        results = []
        query_words = set(query.lower().split())
        
        with Progress() as progress:
            task = progress.add_task("[cyan]Searching...", total=len(self.reference.get("categories", {})))
            
            for category, sections in self.reference.get("categories", {}).items():
                for section in sections:
                    # Combine all searchable fields
                    text_blob = " ".join([
                        section.get("title", ""),
                        section.get("purpose", ""),
                        section.get("syntax", ""),
                        " ".join(section.get("examples", []))
                    ])
                    
                    # Calculate various scores
                    title_score = fuzz.ratio(query.lower(), section.get("title", "").lower())
                    content_score = fuzz.partial_ratio(query.lower(), text_blob.lower())
                    keyword_score = self._calculate_keyword_score(text_blob, query)
                    
                    # Calculate word match score
                    section_words = set(text_blob.lower().split())
                    word_match_score = len(query_words & section_words) / len(query_words) * 100
                    
                    # Weighted combination of scores
                    score = (
                        title_score * 0.4 +  # Title matches are important
                        content_score * 0.3 +  # Content relevance
                        keyword_score * 20 +  # Keyword importance
                        word_match_score * 0.3  # Word overlap
                    )
                    
                    if score > 20:  # Lower threshold for more results
                        results.append({
                            "category": category,
                            "title": section.get("title", ""),
                            "purpose": section.get("purpose", ""),
                            "syntax": section.get("syntax", ""),
                            "examples": section.get("examples", []),
                            "score": score,
                            "scores": {
                                "title": title_score,
                                "content": content_score,
                                "keywords": keyword_score,
                                "word_match": word_match_score
                            }
                        })
                
                progress.update(task, advance=1)

        # Sort by score, descending
        results.sort(key=lambda x: x["score"], reverse=True)
        return results[:top_n]

    def display_results(self, matches, query):
        """Display search results with enhanced formatting."""
        if not matches:
            self.console.print(Panel(
                "No matches found. Try a different query.",
                title="Search Results",
                border_style="yellow"
            ))
            return

        # Display search query
        self.console.print(Panel(
            f"Search Results for: {query}",
            title="Search Results",
            border_style="blue"
        ))
        
        for idx, match in enumerate(matches, 1):
            # Create a table for each result
            table = Table(
                title=f"Result {idx} (Score: {match['score']:.1f}%)",
                box=box.ROUNDED,
                border_style="green"
            )
            
            # Add columns
            table.add_column("Field", style="cyan", width=15)
            table.add_column("Content", style="white")
            
            # Add rows
            table.add_row("Category", match["category"])
            table.add_row("Title", match["title"])
            if match["purpose"]:
                table.add_row("Purpose", match["purpose"])
            if match["syntax"]:
                table.add_row("Syntax", match["syntax"])
            
            # Add detailed scores
            scores_table = Table(box=box.SIMPLE, show_header=False)
            scores_table.add_column("Metric", style="cyan")
            scores_table.add_column("Score", style="yellow")
            for metric, score in match["scores"].items():
                scores_table.add_row(metric.replace("_", " ").title(), f"{score:.1f}%")
            
            # Display the tables
            self.console.print(table)
            self.console.print(Panel(scores_table, title="Match Details", border_style="blue"))
            
            # Display examples with syntax highlighting
            if match["examples"]:
                self.console.print(Panel(
                    "Examples:",
                    title="Examples",
                    border_style="yellow"
                ))
                
                for ex in match["examples"]:
                    # First try to extract and display code blocks
                    code_blocks = self._extract_code_blocks(ex)
                    
                    if code_blocks:
                        for block in code_blocks:
                            # Clean up the code block
                            cleaned_block = block.strip()
                            if cleaned_block:
                                try:
                                    self.console.print(Syntax(
                                        cleaned_block,
                                        "python",
                                        theme="monokai",
                                        line_numbers=True,
                                        word_wrap=True
                                    ))
                                except Exception:
                                    # If syntax highlighting fails, display as regular text
                                    self.console.print(Panel(
                                        cleaned_block,
                                        border_style="yellow",
                                        width=100
                                    ))
                    else:
                        # If no code blocks found, display as regular text
                        self.console.print(Panel(
                            ex.strip(),
                            border_style="yellow",
                            width=100
                        ))
                    
                    # Add a small separator between examples
                    self.console.print()
            
            self.console.print("\n" + "="*100 + "\n")

    def run(self):
        """Run the interactive search interface."""
        self.console.clear()
        self.console.print(Panel(
            "[bold magenta]Python Reference Search[/]\n[italic]Enter your search query (or 'quit' to exit)[/]",
            title="Welcome",
            border_style="magenta"
        ))
        
        while True:
            query = Prompt.ask("\n[bold green]Enter your search query[/]")
            
            if query.lower() == 'quit':
                self.console.print("[yellow]Goodbye![/]")
                break
                
            if not query.strip():
                self.console.print("[red]Please enter a valid search query[/]")
                continue
                
            try:
                matches = self.search(query)
                self.display_results(matches, query)
            except Exception as e:
                self.console.print(f"[red]Error: {str(e)}[/]")

def main():
    # Get the directory of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(current_dir, "new reference", "python_reference.json")
    
    search_app = PythonReferenceSearch(json_path)
    search_app.run()

if __name__ == "__main__":
    main() 