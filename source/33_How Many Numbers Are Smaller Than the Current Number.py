# ta cần 1 mảng đếm các giá trị từ 0 đến 100 -> [0] * 101
# Sau đó mỗi lần gặp số x trong nums, ta tăng count[x] lên 1, tức là đếm tần suất của từng giá trị 0..100
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        # nghiên cứu
        # đếm tần suất
        # count = [0] * 101 # tạo mảng 101 số 0 *5 cũng được -> tạo ra mảng 5 giá trị đề phòng out range
        # for x in nums:
        #     count[x] += 1 # đến số lần xuất hiện của x
        # for i in range(1, 101):
        #     count[i] += count[i - 1] # count[i] = số phần tử trong nums có giá trị ≤ i.
        # Bước 3: trả lời cho từng nums[i]
        # ans = []
        # for x in nums:
        #     if x == 0:
        #         ans.append(0)
        #     else:
        #         ans.append(cnt[x - 1])  # số phần tử < x
        # return ans
        ####
        sorted_nums = sorted(nums)
        count_map = {}
        for i, num in enumerate(sorted_nums):
            if num not in count_map:
                count_map[num] = i
        res = []
        for num in nums:
            smaller_count = count_map[num]
            res.append(smaller_count)
        return res

sol= Solution()
print(sol.smallerNumbersThanCurrent([8,1,2,2,3]))