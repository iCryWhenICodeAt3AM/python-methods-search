"""
Python String Manipulation Guide
==============================

This file contains examples and explanations of string manipulation methods,
searching, replacing, and other string operations in Python.
"""

# ==================== STRING MEMBERSHIP AND COMPARISON ====================

"""
Membership Testing (in, not in)
--------
Purpose: Check if a substring exists in a string
How to use: substring in string, substring not in string
Usable for: Strings
Sample usage:
    text = "Hello, World!"
    contains = "World" in text  # Returns True
    not_contains = "Python" not in text  # Returns True
    
    # Case-sensitive comparison
    "hello" in text  # Returns False
    "hello" in text.lower()  # Returns True
"""

"""
String Comparison
--------
Purpose: Compare strings lexicographically
How to use: string1 < string2, string1 <= string2, etc.
Usable for: Strings
Sample usage:
    # Lexicographical comparison
    "apple" < "banana"  # Returns True
    "cat" > "dog"  # Returns False
    
    # Case matters in comparison
    "Apple" < "banana"  # Returns True (uppercase comes before lowercase)
    
    # Compare with case-insensitive
    "Apple".lower() < "banana".lower()  # Returns True
"""

"""
isalpha(), isdigit(), isalnum()
--------
Purpose: Check if string contains only alphabets/digits/alphanumeric
How to use: string.isalpha(), string.isdigit(), string.isalnum()
Usable for: Strings
Sample usage:
    "Hello".isalpha()  # Returns True
    "123".isdigit()  # Returns True
    "Hello123".isalnum()  # Returns True
    "Hello 123".isalnum()  # Returns False (contains space)
"""

"""
isspace(), islower(), isupper()
--------
Purpose: Check string characteristics
How to use: string.isspace(), string.islower(), string.isupper()
Usable for: Strings
Sample usage:
    "   ".isspace()  # Returns True
    "hello".islower()  # Returns True
    "HELLO".isupper()  # Returns True
    "Hello".islower()  # Returns False
"""

"""
isnumeric(), isdecimal(), isprintable()
--------
Purpose: Check string characteristics
How to use: string.isnumeric(), string.isdecimal(), string.isprintable()
Usable for: Strings
Sample usage:
    "123".isnumeric()  # Returns True
    "123".isdecimal()  # Returns True
    "Hello\n".isprintable()  # Returns False (contains newline)
    "Hello".isprintable()  # Returns True
"""

"""
istitle(), isidentifier()
--------
Purpose: Check if string is title case or valid identifier
How to use: string.istitle(), string.isidentifier()
Usable for: Strings
Sample usage:
    "Hello World".istitle()  # Returns True
    "hello world".istitle()  # Returns False
    "variable_name".isidentifier()  # Returns True
    "123variable".isidentifier()  # Returns False
"""

# ==================== STRING SEARCHING METHODS ====================

"""
find() and rfind()
--------
Purpose: Find the first/last occurrence of a substring
How to use: string.find(substring, start=0, end=len(string))
Usable for: Strings
Sample usage:
    text = "Hello, World! Hello, Python!"
    first = text.find('Hello')  # Returns 0
    last = text.rfind('Hello')  # Returns 13
    not_found = text.find('Python', 0, 10)  # Returns -1
"""

"""
index() and rindex()
--------
Purpose: Find the first/last occurrence of a substring (raises ValueError if not found)
How to use: string.index(substring, start=0, end=len(string))
Usable for: Strings
Sample usage:
    text = "Hello, World! Hello, Python!"
    first = text.index('Hello')  # Returns 0
    last = text.rindex('Hello')  # Returns 13
    # text.index('Python', 0, 10)  # Raises ValueError
"""

"""
count()
--------
Purpose: Count occurrences of a substring
How to use: string.count(substring, start=0, end=len(string))
Usable for: Strings
Sample usage:
    text = "Hello, World! Hello, Python!"
    count = text.count('Hello')  # Returns 2
    count_range = text.count('o', 0, 10)  # Returns 2
"""

"""
startswith() and endswith()
--------
Purpose: Check if string starts/ends with a prefix/suffix
How to use: string.startswith(prefix, start=0, end=len(string))
Usable for: Strings
Sample usage:
    text = "Hello, World!"
    starts = text.startswith('Hello')  # Returns True
    ends = text.endswith('!')  # Returns True
    starts_range = text.startswith('World', 7)  # Returns True
"""

# ==================== STRING REPLACEMENT METHODS ====================

"""
replace()
--------
Purpose: Replace occurrences of a substring
How to use: string.replace(old, new, count=-1)
Usable for: Strings
Sample usage:
    text = "Hello, World! Hello, Python!"
    replaced = text.replace('Hello', 'Hi')  # Returns "Hi, World! Hi, Python!"
    replaced_once = text.replace('Hello', 'Hi', 1)  # Returns "Hi, World! Hello, Python!"
"""

"""
translate() and maketrans()
--------
Purpose: Replace multiple characters using a translation table
How to use: string.translate(table)
Usable for: Strings
Sample usage:
    # Create translation table
    table = str.maketrans('aeiou', '12345')
    text = "Hello, World!"
    translated = text.translate(table)  # Returns "H2ll4, W4rld!"
    
    # Remove specific characters
    remove_chars = str.maketrans('', '', '!,.')
    cleaned = text.translate(remove_chars)  # Returns "Hello World"
"""

# ==================== STRING SPLITTING AND JOINING ====================

"""
split() and rsplit()
--------
Purpose: Split string into a list
How to use: string.split(sep=None, maxsplit=-1)
Usable for: Strings
Sample usage:
    text = "Hello, World, Python"
    parts = text.split(',')  # Returns ['Hello', ' World', ' Python']
    parts = text.split(',', 1)  # Returns ['Hello', ' World, Python']
    words = text.split()  # Returns ['Hello,', 'World,', 'Python']
"""

"""
splitlines()
--------
Purpose: Split string at line boundaries
How to use: string.splitlines(keepends=False)
Usable for: Strings
Sample usage:
    text = "Line 1\nLine 2\r\nLine 3"
    lines = text.splitlines()  # Returns ['Line 1', 'Line 2', 'Line 3']
    lines_with_ends = text.splitlines(True)  # Returns ['Line 1\n', 'Line 2\r\n', 'Line 3']
"""

"""
join()
--------
Purpose: Join elements of an iterable into a string
How to use: string.join(iterable)
Usable for: Lists, tuples, and other iterables
Sample usage:
    words = ['Hello', 'World', 'Python']
    text = ' '.join(words)  # Returns "Hello World Python"
    text = '-'.join(words)  # Returns "Hello-World-Python"
"""

# ==================== STRING CASE MANIPULATION ====================

"""
upper(), lower(), title(), capitalize()
--------
Purpose: Convert string case
How to use: string.upper(), string.lower(), string.title(), string.capitalize()
Usable for: Strings
Sample usage:
    text = "hello, world!"
    upper = text.upper()  # Returns "HELLO, WORLD!"
    lower = text.lower()  # Returns "hello, world!"
    title = text.title()  # Returns "Hello, World!"
    cap = text.capitalize()  # Returns "Hello, world!"
"""

"""
swapcase()
--------
Purpose: Swap case of all characters
How to use: string.swapcase()
Usable for: Strings
Sample usage:
    text = "Hello, World!"
    swapped = text.swapcase()  # Returns "hELLO, wORLD!"
"""

"""
casefold()
--------
Purpose: Convert string to casefolded form (for case-insensitive comparison)
How to use: string.casefold()
Usable for: Strings
Sample usage:
    text = "Hello, World!"
    folded = text.casefold()  # Returns "hello, world!"
    # Useful for case-insensitive comparison
    "Hello".casefold() == "hello".casefold()  # Returns True
"""

# ==================== STRING FORMATTING ====================

"""
strip(), lstrip(), rstrip()
--------
Purpose: Remove leading/trailing whitespace or specified characters
How to use: string.strip(chars=None)
Usable for: Strings
Sample usage:
    text = "  Hello, World!  "
    stripped = text.strip()  # Returns "Hello, World!"
    text = "***Hello***"
    stripped = text.strip('*')  # Returns "Hello"
"""

"""
ljust(), rjust(), center()
--------
Purpose: Pad string to a specified width
How to use: string.ljust(width, fillchar=' ')
Usable for: Strings
Sample usage:
    text = "Hello"
    left = text.ljust(10)  # Returns "Hello     "
    right = text.rjust(10)  # Returns "     Hello"
    center = text.center(10)  # Returns "  Hello   "
    padded = text.center(10, '*')  # Returns "**Hello***"
"""

"""
zfill()
--------
Purpose: Pad string with zeros on the left
How to use: string.zfill(width)
Usable for: Strings
Sample usage:
    text = "42"
    padded = text.zfill(5)  # Returns "00042"
    text = "-42"
    padded = text.zfill(5)  # Returns "-0042"
"""

# ==================== PRACTICAL EXAMPLES ====================

"""
Example: String Validation and Checking
--------
Sample usage:
    # Validate a string
    def validate_string(text):
        if not text:
            return "Empty string"
        if not text.isprintable():
            return "Contains non-printable characters"
        if not text.isalnum():
            return "Contains special characters"
        return "Valid string"
    
    print(validate_string("Hello123"))  # Returns "Valid string"
    print(validate_string("Hello 123"))  # Returns "Contains special characters"
    
    # Check password strength
    def check_password(password):
        if len(password) < 8:
            return "Too short"
        if not any(c.isupper() for c in password):
            return "No uppercase letters"
        if not any(c.islower() for c in password):
            return "No lowercase letters"
        if not any(c.isdigit() for c in password):
            return "No numbers"
        return "Strong password"
    
    print(check_password("abc"))  # Returns "Too short"
    print(check_password("abc123"))  # Returns "No uppercase letters"
    print(check_password("Abc123"))  # Returns "Strong password"
    
    # Find common words in two strings
    def find_common_words(str1, str2):
        words1 = set(str1.lower().split())
        words2 = set(str2.lower().split())
        return words1 & words2  # Returns intersection of sets
    
    text1 = "The quick brown fox"
    text2 = "The lazy brown dog"
    common = find_common_words(text1, text2)
    print(f"Common words: {common}")  # Returns {'the', 'brown'}
""" 