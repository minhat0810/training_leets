class Solution(object):
    def reverseString(self, s):
        l = 0
        r = len(s) - 1
        while r > l:
            s[l], s[r] = s[r],s[l]
            r -= 1
            l += 1
        