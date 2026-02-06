class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        #gán tạm prefix ban đầu là strs[0]
        prefix = strs[0]
        for s in strs[1:]: #chạy từ phần tử số 1
            i = 0
            # i ko dc > prefix     
            # i ko duoc nhieu hon so luong co trong strs
            # prefix tại i phải bằng với s tại i
            while i < len(prefix) and i < len(s) and prefix[i] == s[i]:        
                i += 1
            prefix = prefix[:i] # dịch sang kí tự tiếp theo
            if prefix == "":
                break
        return prefix
        
