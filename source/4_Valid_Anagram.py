class Solution(object):
    def isAnagram(self, s, t):
        #return sorted(s) == sorted(t)
        if len(s) != len(t):
            return False
        hashCount = {}
        for char in s:
            hashCount[char] = hashCount.get(char,0)+ 1 # nếu char chưa có gán = 0; có thì lấy key
            # vd: "sas" đầu ra sẽ là 1 dict với cú pháp: {s:1,a:1} -> {s:2,a:1}
        for char in t:
            # nếu char trong t ko có trong s
            if char not in hashCount:
                return False
            hashCount[char] -= 1
            # nếu char trong t nhiều hơn s
            if hashCount[char]<0:
                return False
        return True
