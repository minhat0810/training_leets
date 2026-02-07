class Solution(object):
    def reversePrefix(self, word, ch):
        if ch not in word:
            return word
        arr = list(word) # chuyển về dạng ["a","b","c","d","e","f","d"]
        l = 0
        for r in range(len(arr)):
            if ch == arr[r]:
                while l < r:
                    # arr[l] = arr[r]
                    # arr[r] = arr[l]
                    arr[l], arr[r] = arr[r], arr[l] # Python cho phép tuple unpacking mếu để như trên ko có temp sẽ sai
                    l += 1
                    r -= 1
                break
        return "".join(arr)
        
        