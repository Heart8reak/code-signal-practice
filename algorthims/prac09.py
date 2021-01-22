'''
Given a string, write a function that returns the index of the first unique (non-repeating) character. If there isn't a unique (non-repeating) character, return -1.

Examples:

csFirstUniqueChar(input_str = "lambdaschool") -> 2
csFirstUniqueChar(input_str = "ilovelambdaschool") -> 0
csFirstUniqueChar(input_str = "vvv") -> -1
Notes:

input_str will only contain lowercase alpha characters.
[execution time limit] 4 seconds (py3)

[input] string input_str

[output] integer
'''

def csFirstUniqueChar(input_str):
    nums = []
    for char in range(len(input_str)):
        nums.append(len([i for i in input_str if i == input_str[char]]))
    if 1 in nums:
        return nums.index(1)
    else: 
        return -1




csFirstUniqueChar(input_str = "lambdaschool")
csFirstUniqueChar(input_str = "ilovelambdaschool")
csFirstUniqueChar(input_str = "vvv")
