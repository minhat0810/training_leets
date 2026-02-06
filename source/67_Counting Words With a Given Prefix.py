class Solution(object):
    def prefixCount(self, words, pref):
        count = 0
        #for word in words:
            # c1
            # n_pref = len(pref)
            # s = word[:n_pref]
            # if s == pref:
            #     count += 1
            #c2
            # if word.startswith(pref):
            #     count += 1
      #  return count
      #c2
        return sum(word.startswith(pref) for word in words)
        