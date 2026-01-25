class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        countMap = {}
        for s in stones:
            countMap[s] = countMap.get(s,0) + 1
        result = 0
        for s in jewels:
            if s in countMap:
                result += countMap[s]
        return result