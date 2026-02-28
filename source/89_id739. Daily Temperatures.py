class Solution(object):
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        stack = []
        res = [0] * n 
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                j = stack.pop()
                res[j] = i - j
            stack.append(i)
        return res
#[73,74,75,71,69,72,76,73]
# i = 0 -> res như đầu, stack = [0]
# i = 1, temp[1] > temp[0] -> j = 0, stack = [], res = [1,0,0,0,0,0,0] ,stack.append = [1]
# i = 2, temp[2] > temp[1] -> j = 1, stack = [], res = [1,1,0,0,0,0,0] ,stack.append = [2]
# i = 3, temp[3] < temp[2] -> stack.append = [2,3]
# i = 4, temp[4] < temp[3] -> stack.append = [2,3,4]
# i = 5, temp[5] > temp[4] -> j = 4, stack = [2,3], res = [1,1,0,0,1,0,0]
# -> temp[5] > temp[3] -> j = 3, stack = [2], res = [1,1,0,2,1,0,0]
# -> dừng while stack = [2,5]
# i = 6, temp[6] > temp[5] -> j = 5, stack = [2], res[5] = 1 
# -> temp[6] > temp[2] -> j = 2, stack = [], res[2] = 4 -> stack rỗng thoát while -> stack = [6]
# res = = [1,1,4,2,1,1,0,0]
# i = 7, t = 73
# Top stack = 6 → nhiệt độ 76
# 73 > 76? Không → không vào while
# Push 7: stack = [6,7]
# res vẫn [1,1,4,2,1,1,0,0]

            
        