# tìm tổng 3 số sao cho gần target nhất
# Sort mảng
# Fix một số i
# Dùng two pointers l, r cho phần còn lại
# So sánh:
# Nếu tổng gần target hơn → cập nhật kết quả
# Tổng < target → l++
# Tổng > target → r--
class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)
        closest = nums[0] + nums[1] + nums[2] # khoảng cách gần nhất tới target
        for i in range(n - 2):
            l = i + 1
            r = n - 1
            while l < r:
                s =  nums[i] + nums[l] + nums[r]

                if abs(s-target) < abs(closest - target):
                    closest = s
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    return s
        return closest
        
        