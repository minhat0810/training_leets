# nếu sort lại sau mỗi lần lặp thì độ phức tạp sẽ tăng lên k.nlogn
# nên ta dùng heapify O(n) ,Mỗi lần pop + push: O(log n), O(n + k log n)
# bởi vì python chỉ có min heap nên phải đổi dấu về âm
# giả sử ta có gifts = [25, 64, 9, 4, 100]
# sau khi đổi heap = [-25, -64, -9, -4, -100]
# -> [-100, -64, -25, -4, -9]
import heapq
import math
class Solution(object):
    def pickGifts(self, gifts, k):
        heap = [ -g for g in gifts ]
        heapq.heapify(heap)

        for _ in range(k):
            largest = -heapq.heappop(heap) # lấy đuôi đổi dấu
            new_val = int(math.sqrt(largest))
            heapq.heappush(heap, -new_val)

        return -sum(heap)
        

        