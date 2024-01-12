 def romanToInt(self, s):
        sum = 0
        obj = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
        }
        for i in range(len(s)-1):
            if(obj[s[i]]<obj[s[i+1]]):
                sum -= obj[s[i]]
            else:
                sum += obj[s[i]]
        return sum + obj[s[-1]]
