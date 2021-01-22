"""
Create a function that given an integer, returns an integer where every digit in the input integer is squared.
Examples:
csSquareAllDigits(9119) -> 811181 because 9^2 = 81, 1^2 = 1, 1^2 = 1, and 9^2 = 81
csSquareAllDigits(2483) -> 416649 because 2^2 = 4, 4^2 = 16, 8^2 = 64, and 3^2 = 9
[execution time limit] 4 seconds (py3)
[input] integer n
[output] integer
[Python 3] Syntax Tips
# Prints help message to the console
# Returns a string
def helloWorld(name):
    print("This prints to the console when you Run Tests")
    return "Hello, " + name
"""

def csSquareAllDigits(n):
    hope = ""
    res = [int(x) for x in str(n)]
    for number in res:
        nala = (number * number)
        nala_String = str(nala)
        hope += nala_String

    return int(hope)

print(csSquareAllDigits(919))
print(csSquareAllDigits(2483))
