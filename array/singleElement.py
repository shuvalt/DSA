def singleNumber(self, nums):
        s = set()
        obj = {}
        for num in nums:
            if(num not in s):
                s.add(num)
                obj[num] = 1
            else:
                obj[num] = 2
        
        for o in obj:
            if(obj[o] == 1):
                return o
