class Solution(object):
    def divideArray(self, nums):
        # freq = {}
        # for num in nums:
        #     freq[num] = freq.get(num,0) + 1
        # for i in freq.values():
        #     if i % 2 == 0:
        #         return True
        # return False
        #c2
        return all( i%2 == 0 for i in Counter(nums).values() )
        