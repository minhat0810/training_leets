class Solution(object):
    def maxArea(self, height):
        l = 0
        r = len(height) - 1
        max_area = 0
        while l < r:
            h = min(height[r],height[l])
            w = r - l
            max_area = max(max_area, h*w)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area
        