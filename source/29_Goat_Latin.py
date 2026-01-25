class Solution(object):
    def toGoatLatin(self, sentence):
        vowels  = set("ueoaiUEOAI")
        words =  sentence.split()

        result = []
        for i, word in enumerate(words,start=1):
            if word[0] in vowels:
                new_word = word + "ma"
            else:
                new_word = word[1:] + word[0] + "ma"
            new_word += "a" * i # vì mỗi từ +1 thêm 1 a vd words = ["I", "speak", "Goat", "Latin"] tương ứng với 4, mỗi từ thêm 1 a -> "Imaa peaksmaaa oatGmaaaa atinLmaaaaa" 
            result.append(new_word)

        return " ".join(result)
sol= Solution()
print(sol.toGoatLatin("goat"))