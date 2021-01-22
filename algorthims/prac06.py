"""
Given two strings that include only lowercase alpha characters, str_1 and str_2, write a function that returns a new sorted string that contains any character (only once) that appeared in str_1 or str_2.
Examples:
csLongestPossible("aabbbcccdef", "xxyyzzz") -> "abcdefxyz"
csLongestPossible("abc", "abc") -> "abc"
[execution time limit] 4 seconds (py3)
[input] string str_1
[input] string str_2
[output] string
"""

def csLongestPossible(str_1, str_2):

    unique_str1 = set(str_1)
    unique_str2 = set(str_2)

    unique_str1.update(unique_str2)

    s = list(unique_str1)
    s.sort()

    return "".join(s)



print(csLongestPossible("aabbbcccdef", "xxyyzzz"))  
print(csLongestPossible("abc", "abc"))

