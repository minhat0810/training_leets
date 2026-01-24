#timeSeries là thời gian teemo sẽ tấn công
#duration là thời gian độc duy trì
# côt lõi là nên Xét khoảng cách giữa 2 đòn liên tiếp gap = timeSeries[i+1] - timeSeries[i]
#Nếu gap >= duration → cộng trọn duration
#Nếu gap < duration → chỉ cộng gap (vì bị chồng)
class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        if not timeSeries:
            return 0
        total = 0
        for i in range(len(timeSeries)-1): # tới phần tử cận cuối
            gap = timeSeries[i+1] - timeSeries[i]
            total = min(gap,duration)
        return total + duration