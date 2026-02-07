class Solution(object):
    def removeElement(self, nums, val):
        nums.sort()
        i = 1
        
        for j in range(1, len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i 
        