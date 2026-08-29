from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq =Counter(nums)
        maxi=0
        ans=0
        for num in freq:
            if maxi<freq[num]:
                maxi=freq[num]
                ans=num
        return ans
        
