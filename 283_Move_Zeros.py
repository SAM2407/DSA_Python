class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i=0
        j=0
        n=len(nums)
        while i<n:
            if(nums[i]!=0):
                nums[i], nums[j] = nums[j], nums[i]
                j+=1
            i+=1
        return nums
