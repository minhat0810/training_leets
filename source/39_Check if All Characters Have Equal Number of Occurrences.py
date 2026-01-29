class Solution(object):
    def areOccurrencesEqual(self, s):
        count = {}
        for i in s:
            count[i] =  count.get(i,0)+1
        
        values = list(count.values()) # lấy value
        return all(v == values[0] for v in values) # so sánh all v với value đầu