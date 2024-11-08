#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data(int): A list of integers, where each integer represents  
 one byte of data.

    Returns:
        True if the input data is a valid UTF-8 encoding, False otherwise.
    """
    expected_byte = check_lead(data[0])
    if expected_byte == 0:
        return False
    elif expected_byte == 1:
        return True
    else:
        return verify(data[1:expected_byte])


def check_lead(num):
    """
    Determine the number of bytes in a UTF-8 character
    based on the leading byte.

    Args:
        num (int): An integer representing a single byte (0-255).

    Returns:
        int:
            - 1 if it's a valid 1-byte character (0xxxxxxx).
            - 2 if it's the start of a valid 2-byte character (110xxxxx).
            - 3 if it's the start of a valid 3-byte character (1110xxxx).
            - 4 if it's the start of a valid 4-byte character (11110xxx).
            - 0 if the byte does not represent a valid UTF-8 leading byte.
    """
    if num & 0b10000000 == 0:
        return 1
    elif num & 0b11100000 == 0b11000000:
        return 2
    elif num & 0b11110000 == 0b11100000:
        return 3
    elif num & 0b11111000 == 0b11110000:
        return 4
    else:
        return 0


def check_others(num):
    """
    Check if a given byte is a valid continuation byte in UTF-8 encoding.

    Args:
        num (int): An integer representing a single byte (0-255).

    Returns:
        bool:
            - True if the byte is a valid continuation byte (10xxxxxx).
            - False if the byte is not a valid continuation byte.
    """
    if num & 0b11000000 == 0b10000000:
        return True
    else:
        return False


def verify(data):
    """
    Verify that all continuation bytes in a UTF-8 character are valid.

    Args:
        data (list of int): A list of integers where
                            each integer represents a byte.

    Returns:
        bool:
            - True if all continuation bytes are valid.
            - False if any byte is not a valid continuation byte.
    """
    for byte in data:
        if not check_others(byte):
            return False
    return True
