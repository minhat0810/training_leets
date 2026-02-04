class Solution(object):
    def countEven(self, num):
        count = 0
        #i = 0
        for i in range(1,num+1):
            sum_digits = sum(int(c) for c in str(i))
            if sum_digits % 2 == 0:
                count += 1
        return count
            

        