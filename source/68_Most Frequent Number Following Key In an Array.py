class Solution(object):
    def mostFrequent(self, nums, key):
        num_maps = {}

        for i in range(len(nums)-1):
            if nums[i] == key:
                target = nums[i+1]
                num_maps[target] = num_maps.get(target, 0) + 1

        return max(num_maps, key = num_maps.get)
                 
        