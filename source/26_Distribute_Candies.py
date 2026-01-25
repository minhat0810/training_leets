class Solution(object):
    def distributeCandies(self, candyType):
        candiesDiffLength = len(set(candyType))
        return min(candiesDiffLength,len(candyType)//2)