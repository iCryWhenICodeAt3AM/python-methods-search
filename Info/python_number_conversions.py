"""
Python Number System Conversions and String Encoding Guide
=======================================================

This file contains examples and explanations of various number system conversions
and string encoding/decoding methods in Python.
"""

# ==================== NUMBER SYSTEM CONVERSIONS ====================

"""
Decimal to Binary
--------
Purpose: Convert decimal number to binary string
How to use: bin(number) or format(number, 'b')
Usable for: Integers
Sample usage:
    decimal = 42
    binary = bin(decimal)  # Returns '0b101010'
    binary_no_prefix = format(decimal, 'b')  # Returns '101010'
    binary_padded = format(decimal, '08b')  # Returns '00101010' (8 digits)
"""

"""
Decimal to Hexadecimal
--------
Purpose: Convert decimal number to hexadecimal string
How to use: hex(number) or format(number, 'x')
Usable for: Integers
Sample usage:
    decimal = 42
    hex_num = hex(decimal)  # Returns '0x2a'
    hex_no_prefix = format(decimal, 'x')  # Returns '2a'
    hex_upper = format(decimal, 'X')  # Returns '2A'
    hex_padded = format(decimal, '04x')  # Returns '002a' (4 digits)
"""

"""
Decimal to Octal
--------
Purpose: Convert decimal number to octal string
How to use: oct(number) or format(number, 'o')
Usable for: Integers
Sample usage:
    decimal = 42
    octal = oct(decimal)  # Returns '0o52'
    octal_no_prefix = format(decimal, 'o')  # Returns '52'
    octal_padded = format(decimal, '04o')  # Returns '0052' (4 digits)
"""

"""
Binary to Decimal
--------
Purpose: Convert binary string to decimal number
How to use: int(binary_string, 2)
Usable for: Binary strings (with or without '0b' prefix)
Sample usage:
    binary = '101010'
    decimal = int(binary, 2)  # Returns 42
    binary_with_prefix = '0b101010'
    decimal2 = int(binary_with_prefix, 2)  # Returns 42
"""

"""
Hexadecimal to Decimal
--------
Purpose: Convert hexadecimal string to decimal number
How to use: int(hex_string, 16)
Usable for: Hex strings (with or without '0x' prefix)
Sample usage:
    hex_str = '2a'
    decimal = int(hex_str, 16)  # Returns 42
    hex_with_prefix = '0x2a'
    decimal2 = int(hex_with_prefix, 16)  # Returns 42
"""

"""
Octal to Decimal
--------
Purpose: Convert octal string to decimal number
How to use: int(octal_string, 8)
Usable for: Octal strings (with or without '0o' prefix)
Sample usage:
    octal = '52'
    decimal = int(octal, 8)  # Returns 42
    octal_with_prefix = '0o52'
    decimal2 = int(octal_with_prefix, 8)  # Returns 42
"""

# ==================== CROSS-CONVERSION METHODS ====================

"""
Binary to Hexadecimal
--------
Purpose: Convert binary string to hexadecimal string
How to use: hex(int(binary_string, 2)) or format(int(binary_string, 2), 'x')
Usable for: Binary strings
Sample usage:
    binary = '101010'
    hex_str = hex(int(binary, 2))  # Returns '0x2a'
    hex_no_prefix = format(int(binary, 2), 'x')  # Returns '2a'
    hex_upper = format(int(binary, 2), 'X')  # Returns '2A'
"""

"""
Binary to Octal
--------
Purpose: Convert binary string to octal string
How to use: oct(int(binary_string, 2)) or format(int(binary_string, 2), 'o')
Usable for: Binary strings
Sample usage:
    binary = '101010'
    octal = oct(int(binary, 2))  # Returns '0o52'
    octal_no_prefix = format(int(binary, 2), 'o')  # Returns '52'
"""

"""
Hexadecimal to Binary
--------
Purpose: Convert hexadecimal string to binary string
How to use: bin(int(hex_string, 16)) or format(int(hex_string, 16), 'b')
Usable for: Hex strings
Sample usage:
    hex_str = '2a'
    binary = bin(int(hex_str, 16))  # Returns '0b101010'
    binary_no_prefix = format(int(hex_str, 16), 'b')  # Returns '101010'
    binary_padded = format(int(hex_str, 16), '08b')  # Returns '00101010'
"""

"""
Hexadecimal to Octal
--------
Purpose: Convert hexadecimal string to octal string
How to use: oct(int(hex_string, 16)) or format(int(hex_string, 16), 'o')
Usable for: Hex strings
Sample usage:
    hex_str = '2a'
    octal = oct(int(hex_str, 16))  # Returns '0o52'
    octal_no_prefix = format(int(hex_str, 16), 'o')  # Returns '52'
"""

"""
Octal to Binary
--------
Purpose: Convert octal string to binary string
How to use: bin(int(octal_string, 8)) or format(int(octal_string, 8), 'b')
Usable for: Octal strings
Sample usage:
    octal = '52'
    binary = bin(int(octal, 8))  # Returns '0b101010'
    binary_no_prefix = format(int(octal, 8), 'b')  # Returns '101010'
    binary_padded = format(int(octal, 8), '08b')  # Returns '00101010'
"""

"""
Octal to Hexadecimal
--------
Purpose: Convert octal string to hexadecimal string
How to use: hex(int(octal_string, 8)) or format(int(octal_string, 8), 'x')
Usable for: Octal strings
Sample usage:
    octal = '52'
    hex_str = hex(int(octal, 8))  # Returns '0x2a'
    hex_no_prefix = format(int(octal, 8), 'x')  # Returns '2a'
    hex_upper = format(int(octal, 8), 'X')  # Returns '2A'
"""

# ==================== STRING ENCODING/DECODING ====================

"""
String to Bytes (UTF-8)
--------
Purpose: Convert string to bytes using UTF-8 encoding
How to use: string.encode('utf-8')
Usable for: Strings
Sample usage:
    text = "Hello, 世界"
    bytes_data = text.encode('utf-8')  # Returns b'Hello, \xe4\xb8\x96\xe7\x95\x8c'
"""

"""
Bytes to String (UTF-8)
--------
Purpose: Convert bytes to string using UTF-8 decoding
How to use: bytes_data.decode('utf-8')
Usable for: Bytes objects
Sample usage:
    bytes_data = b'Hello, \xe4\xb8\x96\xe7\x95\x8c'
    text = bytes_data.decode('utf-8')  # Returns "Hello, 世界"
"""

"""
ASCII Encoding/Decoding
--------
Purpose: Convert string to/from ASCII bytes
How to use: string.encode('ascii') or bytes_data.decode('ascii')
Usable for: ASCII-compatible strings
Sample usage:
    text = "Hello"
    ascii_bytes = text.encode('ascii')  # Returns b'Hello'
    decoded_text = ascii_bytes.decode('ascii')  # Returns "Hello"
"""

"""
Base64 Encoding/Decoding
--------
Purpose: Convert bytes to/from base64 string
How to use: base64.b64encode() or base64.b64decode()
Usable for: Binary data
Sample usage:
    import base64
    data = b'Hello, World!'
    encoded = base64.b64encode(data)  # Returns b'SGVsbG8sIFdvcmxkIQ=='
    decoded = base64.b64decode(encoded)  # Returns b'Hello, World!'
"""

# ==================== BINARY AND STRING CONVERSIONS ====================

"""
String to Binary
--------
Purpose: Convert string to binary representation
How to use: ' '.join(format(ord(char), '08b') for char in string)
Usable for: Any string (ASCII or Unicode)
Sample usage:
    text = "Hello"
    binary = ' '.join(format(ord(char), '08b') for char in text)
    # Returns '01001000 01100101 01101100 01101100 01101111'
    
    # For Unicode characters
    text = "Hello, 世界"
    binary = ' '.join(format(ord(char), '08b') for char in text)
    # Returns '01001000 01100101 01101100 01101100 01101111 00101100 00100000 11100100 10111000 10010110 11100101 10101101 10001100'
"""

"""
Binary to String
--------
Purpose: Convert binary string back to text
How to use: ''.join(chr(int(binary, 2)) for binary in binary_string.split())
Usable for: Binary strings in 8-bit format
Sample usage:
    binary = '01001000 01100101 01101100 01101100 01101111'
    text = ''.join(chr(int(binary, 2)) for binary in binary.split())
    # Returns "Hello"
    
    # For Unicode characters
    binary = '01001000 01100101 01101100 01101100 01101111 00101100 00100000 11100100 10111000 10010110 11100101 10101101 10001100'
    text = ''.join(chr(int(binary, 2)) for binary in binary.split())
    # Returns "Hello, 世界"
"""

"""
String to Binary (Alternative Method)
--------
Purpose: Convert string to binary using bytes
How to use: ' '.join(format(byte, '08b') for byte in string.encode('utf-8'))
Usable for: Any string (ASCII or Unicode)
Sample usage:
    text = "Hello"
    binary = ' '.join(format(byte, '08b') for byte in text.encode('utf-8'))
    # Returns '01001000 01100101 01101100 01101100 01101111'
    
    # For Unicode characters
    text = "Hello, 世界"
    binary = ' '.join(format(byte, '08b') for byte in text.encode('utf-8'))
    # Returns '01001000 01100101 01101100 01101100 01101111 00101100 00100000 11100100 10111000 10010110 11100101 10101101 10001100'
"""

"""
Binary to String (Alternative Method)
--------
Purpose: Convert binary string back to text using bytes
How to use: bytes([int(binary, 2) for binary in binary_string.split()]).decode('utf-8')
Usable for: Binary strings in 8-bit format
Sample usage:
    binary = '01001000 01100101 01101100 01101100 01101111'
    text = bytes([int(binary, 2) for binary in binary.split()]).decode('utf-8')
    # Returns "Hello"
    
    # For Unicode characters
    binary = '01001000 01100101 01101100 01101100 01101111 00101100 00100000 11100100 10111000 10010110 11100101 10101101 10001100'
    text = bytes([int(binary, 2) for binary in binary.split()]).decode('utf-8')
    # Returns "Hello, 世界"
"""

# ==================== PRACTICAL EXAMPLES ====================

"""
Example: Converting between number systems
--------
Sample usage:
    # Decimal to different bases
    num = 42
    print(f"Decimal {num}:")
    print(f"Binary: {bin(num)}")
    print(f"Hex: {hex(num)}")
    print(f"Octal: {oct(num)}")
    
    # Converting back to decimal
    binary = '101010'
    hex_str = '2a'
    octal = '52'
    
    print(f"\nConverting back to decimal:")
    print(f"Binary {binary} -> {int(binary, 2)}")
    print(f"Hex {hex_str} -> {int(hex_str, 16)}")
    print(f"Octal {octal} -> {int(octal, 8)}")
    
    # Cross-conversion examples
    print(f"\nCross-conversion examples:")
    print(f"Binary to Hex: {hex(int(binary, 2))}")
    print(f"Hex to Binary: {bin(int(hex_str, 16))}")
    print(f"Octal to Hex: {hex(int(octal, 8))}")
    print(f"Hex to Octal: {oct(int(hex_str, 16))}")
"""

"""
Example: String encoding/decoding
--------
Sample usage:
    # UTF-8 encoding/decoding
    text = "Hello, 世界"
    encoded = text.encode('utf-8')
    decoded = encoded.decode('utf-8')
    print(f"Original: {text}")
    print(f"Encoded: {encoded}")
    print(f"Decoded: {decoded}")
    
    # Base64 encoding/decoding
    import base64
    data = b'Hello, World!'
    encoded = base64.b64encode(data)
    decoded = base64.b64decode(encoded)
    print(f"\nOriginal: {data}")
    print(f"Base64: {encoded}")
    print(f"Decoded: {decoded}")
"""

"""
Example: String to Binary and Back
--------
Sample usage:
    # Convert string to binary
    text = "Hello, 世界"
    print(f"Original text: {text}")
    
    # Method 1: Using ord() and chr()
    binary1 = ' '.join(format(ord(char), '08b') for char in text)
    print(f"\nMethod 1 - Binary: {binary1}")
    text1 = ''.join(chr(int(binary, 2)) for binary in binary1.split())
    print(f"Method 1 - Back to text: {text1}")
    
    # Method 2: Using bytes
    binary2 = ' '.join(format(byte, '08b') for byte in text.encode('utf-8'))
    print(f"\nMethod 2 - Binary: {binary2}")
    text2 = bytes([int(binary, 2) for binary in binary2.split()]).decode('utf-8')
    print(f"Method 2 - Back to text: {text2}")
""" 