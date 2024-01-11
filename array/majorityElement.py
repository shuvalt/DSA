def majorityElement(self, nums):
        obj = {}
        majority = len(nums) / 2
        for num in nums:
            if(num not in obj):
                obj[num] = 1
            else:
                obj[num] +=1
        for key in obj:
            if(obj[key] > majority):
                return key
        return 0
