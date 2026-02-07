class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n):
            # bỏ trùng cho i
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = n - 1
            while r > l:
                s = nums[i] + nums[l] + nums[r]

                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    # skip trùng l
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    # skip trùng r
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1

                    l += 1
                    r -= 1
        return res
        