 def strStr(self, haystack, needle):
        if(haystack == needle):
            return 0
        l = 0
        r = len(needle)
        while(r<=len(haystack)):
            if(haystack[l:r] == needle):
                return l
            l+=1
            r+=1
        return -1
        
