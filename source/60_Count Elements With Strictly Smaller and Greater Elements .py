class Solution(object):
    def countElements(self, nums):
        if len(nums) < 3:
            return 0
        count = 0
        #nums = sorted(nums)
        # smaller = nums[0]
        # greater = nums[len(nums)-1]
        # for i in range(1,len(nums)-1):
        #     if smaller < nums[i] < greater:
        #         count += 1
        # return count 
        #c2 giảm dpt xuống O(n)
        mn = min(nums)
        mx = max(nums)
        for i in nums:
            if mn < i < mx:
                count +=1
        return count
        