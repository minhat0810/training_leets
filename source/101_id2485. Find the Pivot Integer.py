class Solution(object):
    def pivotInteger(self, n):
        total = n * (n + 1) // 2
        left = 0
        right = n
        while left <= right :
            mid = (left+right) // 2
            square = mid * mid
            if square == total:
                return mid
            elif square < total:
                left = mid + 1
            else:
                right = mid - 1
        return -1