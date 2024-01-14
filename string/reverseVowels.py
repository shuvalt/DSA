def reverseVowels(self, s):
        v = "aeiouAEIOU"
        re = list(s)
        l = 0
        r = len(s)-1
        while(l<r):
            if(re[l] not in v):
                l+=1
            elif(re[r] not in v):
                r-=1
            else:
                temp = re[l] 
                re[l] = re[r]
                re[r] = temp
                l+=1
                r-=1

        return "".join(re) 
