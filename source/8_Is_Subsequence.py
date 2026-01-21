#Khởi tạo i = 0
#Duyệt từng ký tự trong t
#Nếu t[j] == s[i] -> i += 1
#Nếu i == len(s) -> kết thúc sớm
#Sau vòng lặp, kiểm tra i == len(s)
class Solution(object):
    def isSubsequence(self, s):
        i = 0
        for char in t:
            if i < len(s) and s[i] == char:
                i +=1
        return len(s) == i
