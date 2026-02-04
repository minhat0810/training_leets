class Solution(object):
    def sortEvenOdd(self, nums):
        even = sorted(nums[::2]) # cắt từ 0 step 2
        odd = sorted(nums[1::2], reverse = True) # cắt từ 1 step 2

        res = nums[:] # tạo copy của nums
        res[::2] = even
        res[1::2] = odd

        return res
 
        