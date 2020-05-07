"""
Write a method to replace all spaces in string with "%20"
input = "Mr John Smith    ", 12
output = "Mr%20John%20Smith

Approach - Remove all trailing white spaces using string split and then replace all spaces with "%20"
Time Complexity - O(N)
Space Complexity - O(N)
"""


def urlify(st,st_len):
    # Trim the string to remove trailing whitespaces
    st = st.strip()
    st = st.replace(" ","%20")
    return st


# Checking trailing spaces
print(urlify("Mr John Smith    ",12))

# Checking white spaces at start
print(urlify("      My name is John Doe", 18))