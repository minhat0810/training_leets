# dùng xor có tính chất a^a = 0, 0^b=b quy tắc giống nhân 0,1 trong nhị phân
# dùng ord() để chuyển về kiểu số nguyên cho char, vì xor chỉ xử lí số
class Solution(object):
    def findTheDifference(self, s, t):
        result = 0
        for i in s:
            result ^= ord(i)
        for i in t:
            result ^= ord(i)
        return chr(result)