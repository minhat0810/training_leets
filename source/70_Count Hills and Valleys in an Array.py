class Solution(object):
    def countHillValley(self, nums):
        # loại bỏ trùng vì nếu 1,1 thì tính là 1 chứ nếu so sánh thẳng thì sẽ sai
        arr = [nums[0]]
        for x in nums:
            if x != arr[-1]: # x khác phần tử trước đó
                arr.append(x)

        count = 0
        for i in range(1,len(arr)- 1):
            if arr[i] > arr[i-1] and arr[i] > arr[i+ 1] :
                count += 1
            elif arr[i] < arr[i+1]  and arr[i] < arr[i+1] :
                count += 1
        return count
        