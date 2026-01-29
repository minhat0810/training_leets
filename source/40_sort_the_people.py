class Solution(object):
    def sortPeople(self, names, heights):
        people = zip(heights, names)
        people = sorted(people, reverse = True) # sắp xếp giảm dần voiwds reverse=true

        return [name for height,name in people ]

        