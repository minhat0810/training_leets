# cần 1 tổng chứa coin đã dùng
class Solution(object):
    def arrangeCoins(self, n):
        left = 0
        right = n
        while left <= right :
            mid = (left+right) // 2
            total = mid * (mid+1) // 2
            if total == n:
                return mid
            elif total < n:
                left = mid + 1
            else:
                right = mid - 1

        return right
        