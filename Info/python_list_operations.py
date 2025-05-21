"""
Python List Operations and Data Handling Guide
============================================

This file contains examples and explanations of list operations,
data handling, and looping techniques in Python.
"""

# ==================== BASIC LIST OPERATIONS ====================

"""
Creating Lists
--------
Purpose: Different ways to create and initialize lists
How to use: Various list creation methods
Sample usage:
    # Empty list
    empty_list = []
    
    # List with initial values
    numbers = [1, 2, 3, 4, 5]
    
    # List comprehension
    squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
    
    # List from string
    chars = list("Hello")  # ['H', 'e', 'l', 'l', 'o']
    
    # List from range
    numbers = list(range(5))  # [0, 1, 2, 3, 4]
"""

"""
Accessing List Elements
--------
Purpose: Get elements from a list using different methods
How to use: Indexing and slicing
Sample usage:
    numbers = [1, 2, 3, 4, 5]
    
    # Get single element
    first = numbers[0]  # 1
    last = numbers[-1]  # 5
    
    # Slicing
    first_three = numbers[:3]  # [1, 2, 3]
    last_two = numbers[-2:]  # [4, 5]
    middle = numbers[1:4]  # [2, 3, 4]
    
    # Step slicing
    even_indices = numbers[::2]  # [1, 3, 5]
    reverse = numbers[::-1]  # [5, 4, 3, 2, 1]
"""

"""
Adding Elements
--------
Purpose: Add elements to a list
How to use: Various methods to append or insert elements
Sample usage:
    numbers = [1, 2, 3]
    
    # Append single element
    numbers.append(4)  # [1, 2, 3, 4]
    
    # Extend with multiple elements
    numbers.extend([5, 6])  # [1, 2, 3, 4, 5, 6]
    
    # Insert at specific position
    numbers.insert(0, 0)  # [0, 1, 2, 3, 4, 5, 6]
    
    # List concatenation
    numbers = numbers + [7, 8]  # [0, 1, 2, 3, 4, 5, 6, 7, 8]
    
    # Shorthand concatenation
    numbers += [9, 10]  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""

"""
Removing Elements
--------
Purpose: Remove elements from a list
How to use: Various methods to remove elements
Sample usage:
    numbers = [1, 2, 3, 4, 5, 3]
    
    # Remove by value (first occurrence)
    numbers.remove(3)  # [1, 2, 4, 5, 3]
    
    # Remove by index
    popped = numbers.pop(1)  # numbers: [1, 4, 5, 3], popped: 2
    
    # Remove last element
    last = numbers.pop()  # numbers: [1, 4, 5], last: 3
    
    # Clear all elements
    numbers.clear()  # []
    
    # Delete by index
    numbers = [1, 2, 3, 4, 5]
    del numbers[1:3]  # [1, 4, 5]
"""

"""
Updating Elements
--------
Purpose: Modify elements in a list
How to use: Direct assignment and list methods
Sample usage:
    numbers = [1, 2, 3, 4, 5]
    
    # Update single element
    numbers[0] = 10  # [10, 2, 3, 4, 5]
    
    # Update slice
    numbers[1:3] = [20, 30]  # [10, 20, 30, 4, 5]
    
    # Sort in place
    numbers.sort()  # [4, 5, 10, 20, 30]
    
    # Reverse in place
    numbers.reverse()  # [30, 20, 10, 5, 4]
"""

# ==================== LIST COMPREHENSIONS AND GENERATORS ====================

"""
List Comprehensions
--------
Purpose: Create new lists using concise syntax
How to use: [expression for item in iterable if condition]
Sample usage:
    # Basic comprehension
    squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
    
    # With condition
    even_squares = [x**2 for x in range(10) if x % 2 == 0]  # [0, 4, 16, 36, 64]
    
    # Nested comprehension
    matrix = [[i+j for j in range(3)] for i in range(3)]
    # [[0, 1, 2], [1, 2, 3], [2, 3, 4]]
"""

"""
Generator Expressions
--------
Purpose: Create memory-efficient iterators
How to use: (expression for item in iterable if condition)
Sample usage:
    # Basic generator
    squares = (x**2 for x in range(5))
    # Use with next() or in loops
    
    # With condition
    even_squares = (x**2 for x in range(10) if x % 2 == 0)
    
    # Convert to list if needed
    squares_list = list(squares)
"""

# ==================== LIST OPERATIONS AND METHODS ====================

"""
List Operations
--------
Purpose: Common operations on lists
How to use: Built-in functions and methods
Sample usage:
    numbers = [1, 2, 3, 4, 5]
    
    # Length
    length = len(numbers)  # 5
    
    # Count occurrences
    count = numbers.count(3)  # 1
    
    # Find index
    index = numbers.index(3)  # 2
    
    # Check membership
    exists = 3 in numbers  # True
    
    # Sum, min, max
    total = sum(numbers)  # 15
    minimum = min(numbers)  # 1
    maximum = max(numbers)  # 5
"""

"""
List Sorting
--------
Purpose: Sort lists in different ways
How to use: sort() and sorted() methods
Sample usage:
    numbers = [3, 1, 4, 1, 5, 9, 2, 6]
    
    # Sort in place
    numbers.sort()  # [1, 1, 2, 3, 4, 5, 6, 9]
    
    # Sort in reverse
    numbers.sort(reverse=True)  # [9, 6, 5, 4, 3, 2, 1, 1]
    
    # Create new sorted list
    sorted_numbers = sorted(numbers)  # Original unchanged
    
    # Sort by key
    words = ['apple', 'banana', 'cherry']
    words.sort(key=len)  # ['apple', 'cherry', 'banana']
"""

# ==================== LOOPING TECHNIQUES ====================

"""
Basic Looping
--------
Purpose: Different ways to iterate over lists
How to use: for loops and while loops
Sample usage:
    numbers = [1, 2, 3, 4, 5]
    
    # For loop
    for num in numbers:
        print(num)
    
    # While loop
    i = 0
    while i < len(numbers):
        print(numbers[i])
        i += 1
    
    # Enumerate
    for index, value in enumerate(numbers):
        print(f"Index {index}: {value}")
    
    # Range-based loop
    for i in range(len(numbers)):
        print(f"Index {i}: {numbers[i]}")
"""

"""
Advanced Looping
--------
Purpose: Advanced iteration techniques
How to use: zip, enumerate, and other tools
Sample usage:
    # Zip multiple lists
    names = ['Alice', 'Bob', 'Charlie']
    ages = [25, 30, 35]
    for name, age in zip(names, ages):
        print(f"{name} is {age} years old")
    
    # List comprehension with condition
    even_numbers = [x for x in range(10) if x % 2 == 0]
    
    # Generator expression
    sum_squares = sum(x**2 for x in range(10))
    
    # Filter
    even_numbers = list(filter(lambda x: x % 2 == 0, range(10)))
    
    # Map
    squares = list(map(lambda x: x**2, range(10)))
"""

# ==================== PRACTICAL EXAMPLES ====================

"""
Example: List Manipulation Tasks
--------
Sample usage:
    # Remove duplicates while preserving order
    def remove_duplicates(lst):
        return list(dict.fromkeys(lst))
    
    # Flatten nested list
    def flatten(lst):
        return [item for sublist in lst for item in sublist]
    
    # Group items by key
    def group_by(lst, key_func):
        groups = {}
        for item in lst:
            key = key_func(item)
            if key not in groups:
                groups[key] = []
            groups[key].append(item)
        return groups
    
    # Example usage
    numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    unique = remove_duplicates(numbers)  # [1, 2, 3, 4]
    
    nested = [[1, 2], [3, 4], [5, 6]]
    flat = flatten(nested)  # [1, 2, 3, 4, 5, 6]
    
    words = ['apple', 'banana', 'cherry', 'date']
    by_length = group_by(words, len)  # {5: ['apple'], 6: ['banana', 'cherry'], 4: ['date']}
""" 