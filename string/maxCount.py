def maxPower(self, s):
        if(len(s)==1):
            return 1
        current = s[0]
        count = 1
        max_count = 1
        for i in range(1,len(s)):
            if(current == s[i]):
                count +=1
                if(max_count<count):
                    max_count = count
            else:
                current = s[i]
                count = 1
            
        return max_count
