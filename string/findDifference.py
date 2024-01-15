def findTheDifference(self, s, t):
        left = sum([ord(x) for x in s])
        right = sum([ord(x) for x in t])
        return chr(right-left)
