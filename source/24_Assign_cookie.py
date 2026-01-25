#Có trẻ em → mỗi đứa có độ tham lam g[i]
#Có bánh quy → mỗi cái có kích thước s[j]
#Một đứa trẻ chỉ cần 1 cái bánh
#Một cái bánh chỉ cho 1 đứa
#Trẻ hài lòng nếu:
#size_cookie >= greed_child
#Mục tiêu: Cho bánh sao cho số trẻ hài lòng là nhiều nhất
class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        i = 0 #trẻ
        j = 0 #bánh
        count = 0
        while i<len(g) and j<len(s): #khi hết trẻ hoặc hết bánh thì dừng.
            if s[i] >= g[j]:
                count += 1
                i += 1 # qua đứa khác
                j += 1  # dùng bánh này
            else:
                j +=1 # số bánh quá ít không đủ qua đứa
        return count
          