#Duyệt chuỗi theo index
#Nếu index chẵn -> giữ nguyên chữ
#Nếu index lẻ → lấy chữ trước đó + số
#index:  0   1   2   3   4   5
#s    = 'a' '1' 'c' '1' 'e' '1' -> range nên bắt đầu ở 1 nhảy 2
#Dùng ASCII để dịch ký tự
class Solution(object):
    def replaceDigits(self, s):
        s = list(s)  # chuyển sang list để sửa
        for i in range(1,len(s),2):
            s[i] = chr( ord(s[i-1]) + int(s[i]) ) # cộng ord char trước + index rồi chuyển về string
        return "".join(s)
        
        