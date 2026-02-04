class Solution(object):
    def countPairs(self, nums, k):
        from collections import defaultdict

        index = defaultdict(list) # khác với index = {} chỉ ở k cần tạo mảng rỗng if num not in idx: idx[num] = []
        res = 0

        for i, num in enumerate(nums):
            index[num].append(i)
        
        for indices in index.values(): # vd [1,5] [0,6] [2,3,4]
            n = len(indices)
            for i in range(n):
                for j in range(i+1,n):
                    if (indices[i]*indices[j]) % k == 0:
                        res += 1

        return res