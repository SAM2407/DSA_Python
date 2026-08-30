class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi = mini = nums[0]
        a=b=0
        for i in range(len(nums)):
            if nums[i]>maxi:
                maxi= nums[i]
                a=i
            if nums[i]<mini:
                mini = nums[i]
                b=i
        
        leftMax = a+1
        leftMin= b+1
        rightMax = len(nums)-a
        rightMin= len(nums)-b
        ans = min(max(leftMax, leftMin), max(rightMax, rightMin), leftMax + rightMin,leftMin + rightMax)   
        return ans



        
