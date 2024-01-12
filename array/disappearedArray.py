class Solution(object):
    def findDisappearedNumbers(self, nums):
        s = set(nums)
        re = []
        for i in range(1,len(nums)+1):
            if(i not in s):
                re.append(i)
        return re

        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
