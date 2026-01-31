class Solution(object):
    def sumOfUnique(self, nums):
        count_map = {}
        for num in nums:
            count_map[num] = count_map.get(num,0)+1
        sum = 0
        for i in count_map:
            if count_map[i] == 1:
                sum += i
        return sum
        