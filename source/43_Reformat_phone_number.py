class Solution(object):
    def reformatNumber(self, number):
       # number = number.replace("-", "").replace(" ", "")
        digits = "".join(c for c in number if c.isdigit())
        s = len(digits)
        result = []
        i = 0
        while s - i > 4:
            result.append(digits[i:i+3])
            i += 3
        if s-i == 4:
            result.append(digits[i:i+2])
            result.append(digits[i+2:i+4])
        else:
            result.append(digits[i:])
            
        return "-".join(result)