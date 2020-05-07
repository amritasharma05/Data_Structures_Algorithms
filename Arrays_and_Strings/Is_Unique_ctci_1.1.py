"""
Implement an algorithm to determine if a string has all unique characters. What if you can not use additional data
structures

DS used - List
Approach - Used the ASCII value of string to check for unique characters
Time Complexity - O(N)
Space Complexity - O(1)
"""

import collections

def is_unique(st):
    # Assuming string to be ASCII
    if len(st) > 256: # Largest ASCII string length can be 256
        return False
    char_set = [False]*128
    for i in range(len(st)):
        val = ord(st[i])
        if char_set[val]:
            return False
        char_set[val] = True
    return True


print(is_unique("abcdefabc"))
print(is_unique("bcgf"))
print(is_unique("xoyoxoy"))