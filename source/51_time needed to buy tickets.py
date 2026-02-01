class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        time = 0
        for i in range(len(tickets)):
            if i <= k: # i,k là người thứ trong mảng
                time += min(tickets[i], tickets[k]) # người đứng trước k, được mua cùng vòng cuối với k
            else: # đứng sau k, không được mua ở vòng cuối của k
                time += min(tickets[i], tickets[k] - 1)
        return time

        