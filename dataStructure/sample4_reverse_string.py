# Reverse String 

import sample3 

string = " gninreaL nIdekniL htiw tol a nraeL"
reversed_string = ""
s = sample3.Stack()


for char in string:
    s.push(char)
while not s.is_empty():
    reversed_string += s.pop()


print(reversed_string)