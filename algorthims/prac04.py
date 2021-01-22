class Solution:
    '''
    Understand:

    "HELLO" --> "hello"
    "hElLo" --> "hello"
    "hEllo1" --> "he lo1"

    Plan

    Hint 1: all upper-case letters encoding have value > 64 AND < 91
    Hint 2: the lower-case equialentof an upper-case character is it's encoding +32
    Hint 3: you can use ord(x) to get the encoding value of a character.. You can use chr(x) to convert back to a character.

    create a new string
    go through each character in the original string
    if character is an upper-case character, the lower case character is + 32
    return the new string that we just created

    '''


    def toLowerCase(self, str: str) -> str:
        encodedChars = [ord(x) for x in str] # return a list of the encoding values for the string
        for i in range(len(encodedChars)):
            if encodedChars[i] > 64 and encodedChars[i] < 91:
                encodedChars[i] += 32
        decodedChars = [chr(x) for x in encodedChars]
        return ''.join(decodedChars)
