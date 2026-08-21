class Solution(object):
    def singleNumber(self, nums):
        freq ={}

        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]]=0
            freq[nums[i]]+=1
        
        for k in freq:
            if freq[k]==1:
                return k
        
        return 0
        
