class Solution(object):
    def checkValid(self, matrix):
        n = len(matrix) # = 3
        target = set(range(1,n+1)) # tạo ra set {1,2,3}, dùng set vì k quan tâm thứ tự ta chỉ cần tránh trùng
        for row in matrix: # duyệt từng hàng
            if set(row) != target:
                return False
        
        for col in range(n):
            col = [matrix[row][col] for row in range(n)]
            if set(col) != target:
                return False
        return True
# core
# col = [matrix[r][c] for r in range(n)]
# matrix = [
#     [1, 2, 3],
#     [3, 1, 2],
#     [2, 3, 1]
# ]
# n = 3
# col = [
#     matrix[0][0],  # 1
#     matrix[1][0],  # 3
#     matrix[2][0]   # 2
# ]
#=> col = [1, 3, 2]

