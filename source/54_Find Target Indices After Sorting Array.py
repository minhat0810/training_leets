class Solution(object):
    def targetIndices(self, nums, target):
        # nums = sorted(nums, reverse = False)
        # res = []
        # for i,num in enumerate(nums):
        #     if num == target:
        #         res.append(i)
        # return res
        # c2 khong sort mường tượng [ <2 , ==2 , >2 ] chỉ lấy less và equal, less + số lượng equal chính là index equal
        less = 0
        equal = 0
        res = []
        for num in nums:
            if num < target:
                less += 1
            elif num == target: 
                equal += 1 
            # bỏ qua các num lớn hơn
        for i in range(equal):
            res.append(less+i)
        return res
