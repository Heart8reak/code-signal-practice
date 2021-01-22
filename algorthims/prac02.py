class Solution:
    '''
    Understand
    numes = [2,2,1] --> 1

    [1] --> 1

    [2,1,2] --> 1

    Plan 
    Use dictionary to keep track of number of occurences per number 
    Iterate through dictionary and find num that occurs once

    '''

    def singleNumber(self, nums: List[int]) -> int:
        counts = {}
        for n in nums:  # O(n)
            if n not in counts:
                count[n] = 1
            else: 
                counts[n] += 1 
        for (num, numOccurences) in counts.item(): # O(n)
            if numOccurences == 1:
                return num