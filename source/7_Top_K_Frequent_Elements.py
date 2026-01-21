# hướng giải quyết
# 1. đếm tần suất nums → hashmap {number : frequency}
# 2. Gom theo tần suất (Bucket)
#   Tạo mảng bucket độ dài n + 1, bucket[f] chứa các số xuất hiện f lần
#   index = frequency , value = list các số có frequency đó           
#   bucket[1] = [3]
#   bucket[2] = [2]
#   bucket[3] = [1]
# 3: Lấy k phần tử từ tần suất cao xuống thấp

class Solution(object):
    def topKFrequent(self, nums, k):
        # đếm tuần suất
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 0
            freq[i] += 1
        # tạo bucket
        bucket = [[] for _ in range(len(nums)+1)] # n+1 index trong nums

        for num,count in freq.items(): # num,count = key-value
            bucket[count].append(num) # vd freq = {1:3,2:3,3:1} -> bucket = [tại vị trí theo count  [1] #3] và [2]: #2 , [3]: #1
        #3: Lấy k phần tử từ tần suất cao xuống thấp
        result = []
        for i in range(len(bucket)-1, 0, -1): # chạy từ đuôi về
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result
                


        