def removeDuplicates(self, nums):
        s = set()
        k = 0
        for num in nums:
            if(num not in s):
                s.add(num)
                nums.insert(k,num)
                k+=1
        
        return k
