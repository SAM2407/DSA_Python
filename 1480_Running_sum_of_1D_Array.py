class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum =0
        ans=[]
        n = len(nums)
        for i in range(n):
            sum=sum+nums[i]
            ans.append(sum)
        return ans
        
