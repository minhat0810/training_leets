class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        hashmap = {}
        
        # đếm chữ trong hashmap
        for ch in magazine:
            hashmap[ch] = hashmap.get(ch,0) + 1
        
        # Dùng chữ cho ransomNote
        for ch in ransomNote:
            if ch not in hashmap or hashmap[ch] == 0:
                return False
            hashmap[ch] -=1
        return True



sol = Solution()
print(sol.canConstruct("ac","aab"))


        