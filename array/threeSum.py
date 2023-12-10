def threeSum(nums):
        result = []
        nums.sort()
        ptr2 =len(nums)-1
        for j in range(len(nums)):
            ptr1 = j+1
            while(ptr1 < ptr2):
                if(nums[j]+nums[ptr1]+nums[ptr2]==0):
                    result.append([nums[j],nums[ptr1],nums[ptr2]])
                    ptr1 +=1
                    ptr2 -=1
                elif(nums[j]+nums[ptr1]+nums[ptr2]<0):
                    ptr1 += 1
                else:
                    ptr2 -= 1
        print(result)
