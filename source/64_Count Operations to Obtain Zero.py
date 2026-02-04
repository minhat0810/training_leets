class Solution(object):
    def countOperations(self, num1, num2):
        total_op = 0
        while num1 > 0 and num2 >0:
            if num1 >= num2:
                total_op += num1 // num2 # chia lấy phần nguyên: 15//5 = 3
                num1 %= num2
            else: 
                total_op += num2 // num1
                num2 %= num1 
        return total_op