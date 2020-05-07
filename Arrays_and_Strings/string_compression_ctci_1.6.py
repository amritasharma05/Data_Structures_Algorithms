"""
String compression - Implement a method to perform basic string compression using the counts of repeated characters
input -> aabcccaaa
output -> a2b1c3a3
"""


def string_compression(st):
    if len(st) == 0:
        return None
    parts = []
    current_letter = st[0]
    current_count = 0
    for letter in st[1:]:
        if letter == current_letter:
            current_count += 1
        else:
            parts.append(current_letter + str(current_count))
            # Resetting the letter and count
            current_letter = letter
            current_count = 1
    # Appending the last letter
    parts.append(current_letter + str(current_count))
    compressed = "".join(parts)
    if len(compressed) < len(st):
        return compressed
    else:
        return st


print(string_compression("aabcccaaa"))
print(string_compression("aaaabbbbccccccccccaaaaaaaadddeeeeffghijjjkkk"))