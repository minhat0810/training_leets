# bài toán yêu cầu ở n[i] cộng của 4 mảng lại = 0 -> count
# chia đôi 2 nums thành 1 cặp với ct chính a+b+c+d = 0 <=> a+b = -(c+d)
class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        from collections import defaultdict

        countAB = defaultdict(int)
        #$ tính nums1 + nums2
        for a in nums1:
            for b in nums2:
                countAB[a+b] += 1           
        #return countAB ->nếu [1,2],[-2,-1],[-1,2],[0,2] -> {-1: 1, 0: 2, 1: 1})
        result = 0
        for c in nums3:
            for d in nums4:
                result += countAB[-(c+d)] # chủ yếu là truy xuất countAB[tại -(c+d)] cơ bản nó chỉ như là mảng a,b -> counABt[-(-1+0)=1] -> countAB[1] = 1 đã có thì cộng result lên 1
                #c = -1, d = 0 → c + d = -1 → cần a + b = 1 → countAB[1] = 1 → result += 1
                #c = -1, d = 2 → c + d = 1 → cần a + b = -1 → countAB[-1] = 1 → result += 1
                #c = 2, d = 0 → c + d = 2 → cần a + b = -2 → countAB[-2] không có → +0
                #c = 2, d = 2 → c + d = 4 → cần a + b = -4 → countAB[-4] không có → +0
        return result

sol = Solution()
print(sol.fourSumCount([1,2],[-2,-1],[-1,2],[0,2]))