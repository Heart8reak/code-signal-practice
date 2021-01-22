class Solution:
    '''
    Understand
    nums = [2,7,11,15], target = 9 --> [0,1]
    nums = [3,2,4], target = 6 --> [1,2]

    Plan
    Generate all possible pairs untill target is found
    '''

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
