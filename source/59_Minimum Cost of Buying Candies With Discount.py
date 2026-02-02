class Solution(object):
    def minimumCost(self, cost):
        cost = sorted(cost, reverse = True)
        sum = 0
        res = []
        for i in range(len(cost)):
            if (i+1) % 3 != 0:
                sum += cost[i]
        return sum

        