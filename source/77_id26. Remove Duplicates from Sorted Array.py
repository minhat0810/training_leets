#Khi nums[j] != nums[i-1]
#đó là giá trị mới
#ghi vào nums[i]
# ->i += 1
class Solution(object):
    def removeDuplicates(self, nums):
        i = 1 #vị trí ghi (slow pointer)
        for j in range(1,len(nums)): # vị trí duyệt (fast pointer)
            if nums[j] != nums[i-1]:
                nums[i] = nums[j]
                i += 1
        return i
        
sol = Solution()
print(sol.removeDuplicates([0,0,1,1,2,2,3]))

        
        