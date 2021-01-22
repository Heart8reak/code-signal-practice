"""
Given a string of words, return the length of the shortest word(s).
Notes:
The input_strut string will never be empty and you do not need to validate for different data types.
[execution time limit] 4 seconds (py3)
[input_strut] string input_strut_str
[output] integer
[Python 3] Syntax Tips
# Prints help message to the console
# Returns a string
def helloWorld(name):
    print("This prints to the console when you Run Tests")
    return "Hello, " + name
"""

def csShortestWord(input_str):
    # check if input_Str contains a space
    if " " in input_str:
        #if space then
        txt = input_str.split(" ")
    elif "\t" in input_str:
        txt = input_str.split("\t")
    else:
        # return length of input_str
        return len(input_str)

    shortest_len = 99999

    for x in txt:
        if len(x) < shortest_len:
            shortest_len = len(x)
    return shortest_len


print(csShortestWord("Always code as if the guy who ends up maintaining your code will be a violent psychopath who knows where you live"))  
print(csShortestWord("ZxuvWBoofsTUtasPIhsuCJjttHhBuuHZoxZk\tWZxAkjdCqDpML"))
print(csShortestWord("not great programmer; just good programmer with great habits."))