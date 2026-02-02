class Solution(object):
    def capitalizeTitle(self, title):
        res = []
        words = title.split()
        for word in words:
            word = word.lower()
            if len(word) > 2:
                word = word[0].upper() + word[1:] 
            res.append(word)
        return " ".join(res)
        