# core là cắt lấy 3 số đuôi thêm . rồi đảo ngược
# có thể dùng for range đếm count 3 thêm . rồi return
class Solution(object):
    def thousandSeparator(self, n):
        s = str(n)
        parts = []
        
        while s:
            parts.append(s[-3:]) # thêm 3 số đuôi
            s = s[:-3]           # cắt bỏ 3 số đuôi
        
        return '.'.join(parts[::-1])

        