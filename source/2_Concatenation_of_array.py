class Solution(object):
    def getConcatenation(self, nums):
        return nums.append(nums.copy())
        # res = nums[:]
        # res.extend(nums)

sol = Solution()
print(sol.getConcatenation([1,2,3,4]))