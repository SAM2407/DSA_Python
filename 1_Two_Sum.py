class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mp={}
        for i in range(len(nums)):
            rem = target-nums[i]
            if rem in mp:
                return [mp[rem], i]
            
            mp[nums[i]]=i
        return []

        
                
            


        
