#Chỉ lấy digit
#Duyệt từng ký tự trong chuỗi
#Loại trùng
#Sắp xếp giảm dần
#Lấy phần tử thứ 2

class Solution(object):
    def secondHighest(self, s):
        #c1
        #digits = "".join(c for c in s if c.isdigit())
        # first = second = - 1
        # for c in digits:
        #     num = int(c)
        #     if num > first:
        #         second = first
        #         first = num
        #     elif first > num > second:
        #         second = num
        # dùng sort 
        #return second
        digits = set(int(c) for c in s if c.isdigit())
        if len(digits) < 2:
            return -1
        digits = sorted(digits, reverse = True)
        return digits[1]

        