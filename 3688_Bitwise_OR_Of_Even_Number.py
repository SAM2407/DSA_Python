class Solution(object):
    def evenNumberBitwiseORs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=0
        for i in range(len(nums)):
            if nums[i]%2==0:
                a=a|nums[i]
        return a
        
