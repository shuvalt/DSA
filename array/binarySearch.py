class Solution(object):
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums)
        while(left<right):
            mid = (right + left) // 2
            if(nums[mid]<target):
                left = mid+1 
            elif(nums[mid]>target):
                right = mid-1 
            else:
                return mid
        return left
        
        
