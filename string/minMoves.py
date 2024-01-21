def minimumMoves(self, s):
        i = 0
        j = 0
        while(i<len(s)):
            if(s[i]=='X'):
                i+=3
                j+=1
            else:
                i+=1
        return j
