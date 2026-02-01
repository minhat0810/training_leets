# sẽ có 2 trường hợp là nhà số 0 -> nhà cuối là xa nhất hoặc n-1 -> 0 là xa nhất
# ex [1,1,1,6,1,1,1] hoặc [1,1,6,1,1,1,1]
# nên tính 2 trường hợp chạy ngược và xuôi -> lấy max
class Solution(object):
    def maxDistance(self, colors):
        res = 0
        n = len(colors)
        # so nhà 0 với các nhà sau
        for i in range(n-1, -1, -1): # chayj nguoc
            if colors[i] != colors[0]:
                res = i
                break
        # so nhà cuối với các nhà trước
        for i in range(n-1):
            if colors[i] != colors[n-1]:
                res = max(res, n - 1 - i)
                break
        return res
        