"""
3 types of edit that can be performed on strings: insert a character, remove a character or replace a character.
Write a function to check if they are one edit(or zero edits) away

Approach - Iterate through the two strings to check insertion, removal and replacement of characters
Time Complexity - O(N + M)
Space Complexity - O(1)
"""


def replace_a_char(st1,st2):
    is_edited = False
    for char1, char2 in zip(st1,st2):
        if char1 != char2:
            if is_edited:
                return False
            is_edited = True
    return True


def insert_a_char(st1,st2):
    is_edited = False
    i,j = 0,0
    while i < len(st1) and j < len(st2):
        if st1[i] != st2[j]:
            if is_edited:
                return False
            is_edited = True
            j += 1
        else:
            i += 1
            j += 1
    return True


def check_one_way(st1,st2):
    if len(st1) == len(st2):
        return replace_a_char(st1,st2)
    elif len(st1) + 1 == len(st2):
        return insert_a_char(st1,st2)
    elif len(st1) - 1 == len(st2):
        return insert_a_char(st1,st2)
    return False


print(check_one_way("pale","ples"))
print(check_one_way("pales","pale"))
print(check_one_way("pale","bale"))
print(check_one_way("pale","bake"))


