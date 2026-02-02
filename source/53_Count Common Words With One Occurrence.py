class Solution(object):
    def countWords(self, words1, words2):
        res = 0
        w1_map = {}
        w2_map = {}
        for ch in words1:
            w1_map[ch] = w1_map.get(ch,0) + 1
            
        for ch in words2:
            w2_map[ch] = w2_map.get(ch, 0) + 1

        for ch in w1_map:
            if w1_map[ch] == 1 and w2_map.get(ch,0) == 1:
                res += 1
        return res