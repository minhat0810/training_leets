class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        empty = 0
        total = 0
        while numBottles > 0 :
             # uống hết chai đang có
            total += numBottles
            empty += numBottles

            # đổi chai
            numBottles = empty // numExchange
            empty = numBottles % numExchange
        return total

sol = Solution()
print(sol.numWaterBottles(15,4))