# cắt đoạn con dài m, nên vị trí bắt đầu lớn nhất có thể là n-m+1
# haystack = "abcde" (n = 5)
# needle   = "cd"    (m = 2)
# i = 0 → "ab"
# i = 1 → "bc"
# i = 2 → "cd" ok
# i = 3 → "de"

class Solution(object):
    def strStr(self, haystack, needle):
        n,m = len(haystack), len(needle)
        if m == 0:
            return 0
        for i in range(n-m+1): 
            if haystack[i:i+m] == needle: # Cắt substring độ dài m, bắt đầu tại vị trí i
                return i
        return -1