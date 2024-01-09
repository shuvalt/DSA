def plusOne(self, digits):
        n = len(digits) - 1
        total = 0
        for num in digits:
            total  += num*(10**n)
            n-=1
        total +=1
        st = str(total)
        re = []
        for i in st:
            re.append(int(i))
        return re
