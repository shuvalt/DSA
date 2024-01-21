def areNumbersAscending(self, s):
        li = s.split(" ")
        num = [x for x in li if x.isnumeric()]
        for i in range(0,len(num)-1):
            if(int(num[i])>=int(num[i+1])):
                return False
        return True
