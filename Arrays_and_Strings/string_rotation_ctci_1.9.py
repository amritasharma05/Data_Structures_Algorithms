"""
String Rotation: Check if one word is a substring of another. Given 2 strings s1 and s2, write a code to check if s2 is
a rotation of s1 using one call isSubstring
Time Complexity - O(N)
Space Complexity - O(N)
"""


def is_rotation(st,sub_st):
    return st.find(sub_st) != -1


def isSubstring(st1, st2):
    if len(st1) == len(st2) != 0:
        return is_rotation(st1+st2,st2)
    return False


print(isSubstring("waterbottle","erbottlewat"))
print(isSubstring("abcdefghijk","defghiabc"))