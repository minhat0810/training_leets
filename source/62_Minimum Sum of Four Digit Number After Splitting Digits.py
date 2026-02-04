class Solution(object):
    def minimumSum(self, num):
        num = sorted( list(map(int,str(num))) ) #chuyển num thành string, sau đó map int - str thành chữ sang số, list để chuyển thành danh sách
        return num[0]*10 + num[2] + num[1]*10 + num[3]
        # vì index 1 sẽ nhỏ hơn 2 để tạo thành số nhỏ hơn 