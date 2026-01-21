#Muốn trồng được thì:
#ô hiện tại = 0
#ô bên trái = 0 hoặc không tồn tại
#ô bên phải = 0 hoặc không tồn tại
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        length = len(flowerbed)
        for i in range(length):
            if flowerbed[i] == 0:
                left = (i == 0) or (flowerbed[i-1] == 0)
                right = (i == length-1) or (flowerbed[i+1] == 0)
                if left and right:
                    flowerbed[i] = 1
                    n -= 1
                    if n == 0:
                        return True
        return n <= 0
        