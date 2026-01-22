class Solution(object):
    def plusOne(self, digits):
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits # ở đây là nối chuỗi, vd [1] + [0,0,0] = [1,0,0,0]

sol = Solution()
print(sol.plusOne([9,9,9]))