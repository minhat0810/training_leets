# để giải quyết ta cần chuẩn hóa về index 0->n-1 sau đó đảo số âm tại các index đó
# nếu vị trí đó chưa âm thì đổi, đã âm thì bỏ qua
# cuối cùng +1 lại để trả về số chưa có 
#Index: 0 1 2 3 4 5 6 7
#Nums:  4 3 2 7 8 2 3 1
#i = 0 -> nums[0] = 4 -> idx = 4 - 1 = 3 -> Đánh dấu nums[3] = 7 -> đảo âm = -7
#i = 1 -> nums[1] = 3 -> idx = 3 - 1 = 2 -> Đánh dấu nums[2] = 2 -> đảo âm = -2
#i = 2 -> nums[2] = -2(do ở trên) -> abs lại là 2 -> idx = 2 - 1 = 1 -> Đánh dấu nums[1] = 3 -> đảo âm = -3
#i = 3 -> nums[3] = 7 -> idx = 7 - 1 = 6 -> Đánh dấu nums[6] = 3 -> đảo âm = -3
#i = 4 -> nums[4] = 8 -> idx = 8 - 1 = 7 -> Đánh dấu nums[7] = 1 -> đảo âm = -1
#i = 5 -> nums[5] = 2 -> idx = 2-1 = 1 n-> nums[1] đã âm không đổi ( ta đang check index khác với i ỏ dòng 3)
#i = 6 -> nums[6] = -3 -> idx = 3 - 1 = 2 -> num[2] đã âm không đổi


class Solution(object):
    def findDisappearedNumbers(self, nums):
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]
            
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)

        return result



sol = Solution()
print(sol.findDisappearedNumbers([4,3,2,7,8,2,3,1]))