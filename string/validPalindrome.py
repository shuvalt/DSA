def isPalindrome(self, s):
        if(len(s)== 0 or len(s) == 1):
            return True
        l = 0
        r = len(s)-1
        while(l<=r):
            start = s[l]
            end = s[r]
            if(not start.isalnum()):
                l+=1
            elif(not end.isalnum()):
                r-=1
            else:
                if(start.lower() != end.lower()):
                    return False
                l+=1
                r-=1
        return True
