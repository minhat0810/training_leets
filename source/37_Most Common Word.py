class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        
        paragraph = paragraph.lower()
        words = paragraph.split()

        banned_set = set(banned)
        count = {}
        
        for word in words:
            if word not in banned_set:
                count[word] = count.get(word, 0) + 1

        max_word = ""
        max_freq = 0
        for word in count:
            if count[word] > max_freq:
                max_freq = count[word]
                max_word = word
        
        # return max(count, key=count.get)
        return max_word