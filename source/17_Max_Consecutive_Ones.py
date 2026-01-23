class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        maxNum = 0
        current = 0
        for num in nums:
            if num == 1:
                current += 1
                maxNum = max(maxNum, current)
            else:
                current = 0
        return maxNum

