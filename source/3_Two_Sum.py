class Solution(object):
    def twoSum(self, nums, target):
        hashMap = {}
        for i,num in enumerate(nums):
        # for i in range(len(nums)):
        #     num = nums[i]
            need = target - num
            if need in hashMap:
                return [hashMap[need],i]
            hashMap[num] = i #thêm cặp key-value vào dict
#seen = {}
#seen[5] = 0
#seen[7] = 1
#{5: 0, 7: 1}                              
sol = Solution()
print(sol.twoSum([1,2,3,4],4))