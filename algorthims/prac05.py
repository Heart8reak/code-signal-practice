"""
Given an array of integers, return the sum of all the positive integers in the array.
Examples:
csSumOfPositive([1, 2, 3, -4, 5]) -> 1 + 2 + 3 + 5 = 11
csSumOfPositive([-3, -2, -1, 0, 1]) -> 1
csSumOfPositive([-3, -2]) -> 0
Notes:
If the input_arr does not contain any positive integers, the default sum should be 0.
[execution time limit] 4 seconds (py3)
[input] array.integer input_arr
[output] integer
[Python 3] Syntax Tips
# Prints help message to the console
# Returns a string
def helloWorld(name):
    print("This prints to the console when you Run Tests")
    return "Hello, " + name
"""

def csSumOfPositive(input_arr):
    pos_nos = [x for x in input_arr if x >= 0]
    return sum(pos_nos)


print(csSumOfPositive([1, 2, 3, -4, 5])) 
print(csSumOfPositive([-3, -2, -1, 0, 1]))  
print(csSumOfPositive([-3, -2])) 