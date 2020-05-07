"""
Write a function to check if it is a permutation of a palindrome. Palindrome might not be limited to just dictionary words
input - Tact Coa
output - True (Permutations: "taco cat", "atco cta")

Approach
1. Use set to keep unique character of strings
2. Iterate through the string to know if char already present in set, if yes remove
3. Else add to set
4. return true if string has 1 or less characters

Time Complexity - O(N)
Space Complexity - O(1)
"""


def check_palindrome_permutation(st):
    char_set = set()
    st = st.replace(" ","").lower()
    for char in st:
        if char in char_set:
            char_set.remove(char)
        else:
            char_set.add(char)
    return len(char_set) <= 1


print(check_palindrome_permutation("Tact Coa"))
print(check_palindrome_permutation("Bal boa"))
