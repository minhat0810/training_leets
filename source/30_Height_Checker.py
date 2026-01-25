class Solution(object):
    def heightChecker(self, heights):
        sortHeigth = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != sortHeigth[i]:
                count += 1
        return count