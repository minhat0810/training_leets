class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()
        l = 0
        r = len(people)-1
        res = 0
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1 # ghép 2 người ok
            r -= 1 # luôn giảm vì là ng nặng nhất, có ghép hay không cũng đã lên thuyền
            res += 1
        return res

        