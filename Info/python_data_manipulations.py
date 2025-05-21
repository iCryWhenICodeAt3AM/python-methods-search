"""
Python Data Structure Manipulations Guide
=======================================

This file contains examples and explanations of advanced data structure manipulations,
list comprehensions, and data type operations in Python.
"""

# ==================== LIST COMPREHENSIONS AND GENERATORS ====================

"""
Basic List Comprehension
--------
Purpose: Create a new list by applying an expression to each item in an iterable
How to use: [expression for item in iterable]
Usable for: Lists, tuples, strings, and other iterables
Sample usage:
    # Square numbers
    numbers = [1, 2, 3, 4, 5]
    squares = [n**2 for n in numbers]  # Returns [1, 4, 9, 16, 25]
    
    # Convert to uppercase
    words = ['hello', 'world']
    upper_words = [word.upper() for word in words]  # Returns ['HELLO', 'WORLD']
"""

"""
List Comprehension with Condition
--------
Purpose: Create a new list by applying an expression to filtered items
How to use: [expression for item in iterable if condition]
Usable for: Lists, tuples, strings, and other iterables
Sample usage:
    # Even numbers only
    numbers = [1, 2, 3, 4, 5, 6]
    evens = [n for n in numbers if n % 2 == 0]  # Returns [2, 4, 6]
    
    # Words longer than 3 characters
    words = ['cat', 'dog', 'elephant', 'bird']
    long_words = [word for word in words if len(word) > 3]  # Returns ['elephant', 'bird']
"""

"""
Nested List Comprehension
--------
Purpose: Create a new list using nested loops
How to use: [expression for item1 in iterable1 for item2 in iterable2]
Usable for: Nested data structures
Sample usage:
    # Create a multiplication table
    table = [[i * j for j in range(1, 4)] for i in range(1, 4)]
    # Returns [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
    
    # Flatten a 2D list
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flat = [num for row in matrix for num in row]  # Returns [1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

"""
Generator Expressions
--------
Purpose: Create an iterator that generates values on demand
How to use: (expression for item in iterable)
Usable for: Large datasets where memory efficiency is important
Sample usage:
    # Sum of squares
    numbers = [1, 2, 3, 4, 5]
    sum_squares = sum(n**2 for n in numbers)  # Returns 55
    
    # Find first match
    numbers = [1, 2, 3, 4, 5]
    first_even = next(n for n in numbers if n % 2 == 0)  # Returns 2
"""

# ==================== DICTIONARY COMPREHENSIONS ====================

"""
Basic Dictionary Comprehension
--------
Purpose: Create a new dictionary by applying expressions to keys and values
How to use: {key_expression: value_expression for item in iterable}
Usable for: Lists, tuples, and other iterables
Sample usage:
    # Square numbers as dictionary
    numbers = [1, 2, 3, 4, 5]
    squares_dict = {n: n**2 for n in numbers}
    # Returns {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    
    # Word lengths
    words = ['cat', 'dog', 'elephant']
    length_dict = {word: len(word) for word in words}
    # Returns {'cat': 3, 'dog': 3, 'elephant': 8}
"""

"""
Dictionary Comprehension with Condition
--------
Purpose: Create a new dictionary with filtered items
How to use: {key: value for item in iterable if condition}
Usable for: Lists, tuples, and other iterables
Sample usage:
    # Only even numbers
    numbers = [1, 2, 3, 4, 5, 6]
    even_squares = {n: n**2 for n in numbers if n % 2 == 0}
    # Returns {2: 4, 4: 16, 6: 36}
    
    # Words longer than 3 characters
    words = ['cat', 'dog', 'elephant', 'bird']
    long_words = {word: len(word) for word in words if len(word) > 3}
    # Returns {'elephant': 8, 'bird': 4}
"""

# ==================== SET COMPREHENSIONS ====================

"""
Set Comprehension
--------
Purpose: Create a new set by applying an expression to each item
How to use: {expression for item in iterable}
Usable for: Lists, tuples, strings, and other iterables
Sample usage:
    # Unique squares
    numbers = [1, 2, 2, 3, 3, 3]
    unique_squares = {n**2 for n in numbers}  # Returns {1, 4, 9}
    
    # Unique word lengths
    words = ['cat', 'dog', 'elephant', 'bird']
    unique_lengths = {len(word) for word in words}  # Returns {3, 4, 8}
"""

# ==================== ADVANCED DATA MANIPULATIONS ====================

"""
List Operations with zip()
--------
Purpose: Combine multiple iterables into a single iterable of tuples
How to use: zip(iterable1, iterable2, ...)
Usable for: Lists, tuples, and other iterables
Sample usage:
    # Combine two lists
    names = ['Alice', 'Bob', 'Charlie']
    ages = [25, 30, 35]
    combined = list(zip(names, ages))
    # Returns [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
    
    # Unzip
    pairs = [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
    names, ages = zip(*pairs)
    # Returns ('Alice', 'Bob', 'Charlie'), (25, 30, 35)
"""

"""
List Operations with enumerate()
--------
Purpose: Add indices to iterable items
How to use: enumerate(iterable, start=0)
Usable for: Lists, tuples, strings, and other iterables
Sample usage:
    # Add indices to list
    words = ['cat', 'dog', 'elephant']
    indexed = list(enumerate(words))
    # Returns [(0, 'cat'), (1, 'dog'), (2, 'elephant')]
    
    # Start from 1
    indexed = list(enumerate(words, start=1))
    # Returns [(1, 'cat'), (2, 'dog'), (3, 'elephant')]
"""

"""
List Operations with filter()
--------
Purpose: Create an iterator of elements that satisfy a condition
How to use: filter(function, iterable)
Usable for: Lists, tuples, and other iterables
Sample usage:
    # Filter even numbers
    numbers = [1, 2, 3, 4, 5, 6]
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    # Returns [2, 4, 6]
    
    # Filter non-empty strings
    words = ['', 'cat', '', 'dog', '']
    non_empty = list(filter(None, words))
    # Returns ['cat', 'dog']
"""

"""
List Operations with map()
--------
Purpose: Apply a function to each item in an iterable
How to use: map(function, iterable)
Usable for: Lists, tuples, and other iterables
Sample usage:
    # Square numbers
    numbers = [1, 2, 3, 4, 5]
    squares = list(map(lambda x: x**2, numbers))
    # Returns [1, 4, 9, 16, 25]
    
    # Convert to uppercase
    words = ['hello', 'world']
    upper_words = list(map(str.upper, words))
    # Returns ['HELLO', 'WORLD']
"""

# ==================== PRACTICAL EXAMPLES ====================

"""
Example: Complex Data Transformations
--------
Sample usage:
    # Create a dictionary of word frequencies
    text = "the quick brown fox jumps over the lazy dog"
    words = text.split()
    word_freq = {word: words.count(word) for word in set(words)}
    print(f"Word frequencies: {word_freq}")
    
    # Find common elements in two lists
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    common = [x for x in list1 if x in list2]
    print(f"Common elements: {common}")
    
    # Create a matrix transpose
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    print(f"Transposed matrix: {transpose}")
    
    # Group items by a key
    items = [('apple', 'fruit'), ('banana', 'fruit'), ('carrot', 'vegetable')]
    grouped = {}
    for item, category in items:
        grouped.setdefault(category, []).append(item)
    print(f"Grouped items: {grouped}")
""" 