class Solution(object):
    def removeDuplicates(self, nums):
        j=0
        i=1
        n=len(nums)
        count=0
        for i in range(n):
            if nums[j]!=nums[i]:
                j+=1
                nums[j]=nums[i]
        return j+1
        
