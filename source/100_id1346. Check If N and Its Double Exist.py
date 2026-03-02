class Solution(object):
    def checkIfExist(self, arr):
        arr.sort()
        n = len(arr) 
        for i in range(n):
            target = 2 * arr[i]
            left = 0
            right = n - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == target:
                    if mid != i:
                        return True  # đảm bảo khác index
                    else:
                        break # tránh lặp vô hạn
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
        return False