"""
Python Methods Reference Guide
=============================

This file contains a comprehensive reference of commonly used Python methods and functions,
organized by category with examples and usage notes.
"""

# ==================== BUILT-IN FUNCTIONS ====================

"""
sum()
--------
Purpose: Calculate the sum of all items in an iterable
How to use: sum(iterable, start=0)
Usable for: Lists, tuples, sets, and other iterables containing numbers
Sample usage:
    numbers = [1, 2, 3, 4, 5]
    total = sum(numbers)  # Returns 15
    total_with_start = sum(numbers, 10)  # Returns 25
"""

"""
len()
--------
Purpose: Return the length (number of items) of an object
How to use: len(object)
Usable for: Strings, lists, tuples, dictionaries, sets
Sample usage:
    text = "Hello"
    length = len(text)  # Returns 5
    my_list = [1, 2, 3]
    list_length = len(my_list)  # Returns 3
"""

"""
sorted()
--------
Purpose: Return a new sorted list from the items in iterable
How to use: sorted(iterable, key=None, reverse=False)
Usable for: Lists, tuples, strings, and other iterables
Sample usage:
    numbers = [3, 1, 4, 1, 5]
    sorted_nums = sorted(numbers)  # Returns [1, 1, 3, 4, 5]
    sorted_desc = sorted(numbers, reverse=True)  # Returns [5, 4, 3, 1, 1]
"""

"""
max() and min()
--------
Purpose: Return the largest/smallest item in an iterable
How to use: max(iterable, key=None) or min(iterable, key=None)
Usable for: Lists, tuples, sets, and other iterables
Sample usage:
    numbers = [1, 2, 3, 4, 5]
    maximum = max(numbers)  # Returns 5
    minimum = min(numbers)  # Returns 1
"""

# ==================== LIST METHODS ====================

"""
append()
--------
Purpose: Add an element to the end of the list
How to use: list.append(element)
Usable for: Lists
Sample usage:
    my_list = [1, 2, 3]
    my_list.append(4)  # my_list becomes [1, 2, 3, 4]
"""

"""
extend()
--------
Purpose: Extend list by appending elements from the iterable
How to use: list.extend(iterable)
Usable for: Lists
Sample usage:
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    list1.extend(list2)  # list1 becomes [1, 2, 3, 4, 5, 6]
"""

"""
insert()
--------
Purpose: Insert an element at a specified position
How to use: list.insert(index, element)
Usable for: Lists
Sample usage:
    my_list = [1, 2, 3]
    my_list.insert(1, 'x')  # my_list becomes [1, 'x', 2, 3]
"""

"""
remove()
--------
Purpose: Remove first occurrence of value
How to use: list.remove(value)
Usable for: Lists
Sample usage:
    my_list = [1, 2, 3, 2]
    my_list.remove(2)  # my_list becomes [1, 3, 2]
"""

"""
pop()
--------
Purpose: Remove and return item at index (default last)
How to use: list.pop(index=-1)
Usable for: Lists
Sample usage:
    my_list = [1, 2, 3]
    last = my_list.pop()  # Returns 3, my_list becomes [1, 2]
    first = my_list.pop(0)  # Returns 1, my_list becomes [2]
"""

"""
index()
--------
Purpose: Return first index of value
How to use: list.index(value, start=0, end=len(list))
Usable for: Lists
Sample usage:
    my_list = [1, 2, 3, 2]
    index = my_list.index(2)  # Returns 1
"""

"""
count()
--------
Purpose: Return number of occurrences of value
How to use: list.count(value)
Usable for: Lists
Sample usage:
    my_list = [1, 2, 2, 3, 2]
    count = my_list.count(2)  # Returns 3
"""

"""
sort()
--------
Purpose: Sort the list in place
How to use: list.sort(key=None, reverse=False)
Usable for: Lists
Sample usage:
    my_list = [3, 1, 4, 1, 5]
    my_list.sort()  # my_list becomes [1, 1, 3, 4, 5]
    my_list.sort(reverse=True)  # my_list becomes [5, 4, 3, 1, 1]
"""

"""
reverse()
--------
Purpose: Reverse the list in place
How to use: list.reverse()
Usable for: Lists
Sample usage:
    my_list = [1, 2, 3]
    my_list.reverse()  # my_list becomes [3, 2, 1]
"""

# ==================== STRING METHODS ====================

"""
upper() and lower()
--------
Purpose: Convert string to uppercase/lowercase
How to use: string.upper() or string.lower()
Usable for: Strings
Sample usage:
    text = "Hello"
    upper_text = text.upper()  # Returns "HELLO"
    lower_text = text.lower()  # Returns "hello"
"""

"""
strip(), lstrip(), rstrip()
--------
Purpose: Remove leading/trailing whitespace or specified characters
How to use: string.strip(chars=None)
Usable for: Strings
Sample usage:
    text = "  Hello  "
    stripped = text.strip()  # Returns "Hello"
    text2 = "***Hello***"
    stripped2 = text2.strip('*')  # Returns "Hello"
"""

"""
split()
--------
Purpose: Split string into a list
How to use: string.split(sep=None, maxsplit=-1)
Usable for: Strings
Sample usage:
    text = "Hello,World,Python"
    parts = text.split(',')  # Returns ['Hello', 'World', 'Python']
"""

"""
join()
--------
Purpose: Join elements of an iterable into a string
How to use: string.join(iterable)
Usable for: Strings
Sample usage:
    words = ['Hello', 'World']
    text = ' '.join(words)  # Returns "Hello World"
"""

"""
replace()
--------
Purpose: Replace occurrences of substring
How to use: string.replace(old, new, count=-1)
Usable for: Strings
Sample usage:
    text = "Hello World"
    new_text = text.replace('World', 'Python')  # Returns "Hello Python"
"""

"""
startswith() and endswith()
--------
Purpose: Check if string starts/ends with specified prefix/suffix
How to use: string.startswith(prefix) or string.endswith(suffix)
Usable for: Strings
Sample usage:
    text = "Hello World"
    starts = text.startswith('Hello')  # Returns True
    ends = text.endswith('World')  # Returns True
"""

# ==================== DICTIONARY METHODS ====================

"""
get()
--------
Purpose: Return value for key if key exists, else default
How to use: dict.get(key, default=None)
Usable for: Dictionaries
Sample usage:
    my_dict = {'a': 1, 'b': 2}
    value = my_dict.get('a')  # Returns 1
    value = my_dict.get('c', 0)  # Returns 0
"""

"""
keys(), values(), items()
--------
Purpose: Return view of dictionary's keys/values/key-value pairs
How to use: dict.keys(), dict.values(), dict.items()
Usable for: Dictionaries
Sample usage:
    my_dict = {'a': 1, 'b': 2}
    keys = my_dict.keys()  # Returns dict_keys(['a', 'b'])
    values = my_dict.values()  # Returns dict_values([1, 2])
    items = my_dict.items()  # Returns dict_items([('a', 1), ('b', 2)])
"""

"""
update()
--------
Purpose: Update dictionary with key/value pairs
How to use: dict.update(other_dict)
Usable for: Dictionaries
Sample usage:
    dict1 = {'a': 1}
    dict2 = {'b': 2}
    dict1.update(dict2)  # dict1 becomes {'a': 1, 'b': 2}
"""

"""
pop()
--------
Purpose: Remove specified key and return corresponding value
How to use: dict.pop(key, default)
Usable for: Dictionaries
Sample usage:
    my_dict = {'a': 1, 'b': 2}
    value = my_dict.pop('a')  # Returns 1, my_dict becomes {'b': 2}
"""

# ==================== SET METHODS ====================

"""
add()
--------
Purpose: Add element to set
How to use: set.add(element)
Usable for: Sets
Sample usage:
    my_set = {1, 2, 3}
    my_set.add(4)  # my_set becomes {1, 2, 3, 4}
"""

"""
remove() and discard()
--------
Purpose: Remove element from set (remove raises KeyError if not found)
How to use: set.remove(element) or set.discard(element)
Usable for: Sets
Sample usage:
    my_set = {1, 2, 3}
    my_set.remove(2)  # my_set becomes {1, 3}
    my_set.discard(4)  # No error if 4 not in set
"""

"""
union(), intersection(), difference()
--------
Purpose: Return new set with elements from both sets/only in both/only in first
How to use: set1.union(set2), set1.intersection(set2), set1.difference(set2)
Usable for: Sets
Sample usage:
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    union = set1.union(set2)  # Returns {1, 2, 3, 4, 5}
    intersection = set1.intersection(set2)  # Returns {3}
    difference = set1.difference(set2)  # Returns {1, 2}
""" 