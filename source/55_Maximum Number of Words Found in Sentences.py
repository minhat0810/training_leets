class Solution(object):
    def mostWordsFound(self, sentences):
        max_words = 0
        for i in sentences:
            words = i.split()
            max_words = max(max_words,len(words))
        return max_words
        