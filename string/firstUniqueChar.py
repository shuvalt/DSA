def firstUniqChar(self, s):
        toCheck = {}
        for char in s:
            if(char not in toCheck):
                toCheck[char] = 1
            else:
                toCheck[char] += 1
        for char in s:
            if(toCheck[char] == 1):
                return s.index(char)
        return -1
