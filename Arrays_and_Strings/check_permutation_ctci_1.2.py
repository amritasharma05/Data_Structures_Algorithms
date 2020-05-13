"""
Given two strings, write a method to decide if one is a permutation of other

Approach - Sort the string using in-built sorted function which uses Timsort algorithm under the hood
Time Complexity - O(nlogn)
Space Complexity - O(1)
"""


def is_permutation(st1,st2):
    return sorted(st1) == sorted(st2)

print(is_permutation("chaplin","linchap"))
print(is_permutation("charlie","churlie"))