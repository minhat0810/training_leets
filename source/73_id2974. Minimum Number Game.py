class Solution(object):
    def numberGame(self, nums):
        res = []
        nums.sort()
        for i in range(0,len(nums),2):
            res.append(nums[i+1])
            res.append(nums[i])
            nums
        return res
        