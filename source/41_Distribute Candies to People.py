#Ý tưởng
#Tạo mảng res độ dài num_people, ban đầu toàn 0
#Dùng biến:
#give = 1 (số kẹo sẽ phát)
#i (vị trí người nhận, xoay vòng bằng %)
#Mỗi vòng:
#Phát min(give, candies)
#Trừ kẹo
#Tăng give
#Sang người tiếp theo
class Solution(object):
    def distributeCandies(self, candies, num_people):
        result = [0] * num_people
        give = 1
        i = 0

        while candies>0:
            result[i] += min(give, candies)
            candies -= give
            give += 1
            i = (i+1) % num_people
        return result
        

        