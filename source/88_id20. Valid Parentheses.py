class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for ch in s:
            if ch in mapping.values():
                stack.append(ch)
            else:
                if not stack or stack.pop() != mapping[ch]:
                    return False
        return len(stack) == 0

        
        