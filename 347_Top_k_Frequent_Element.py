from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = Counter(nums)
        ans=[]
        for i, count in freq.most_common(k):
            ans.append(i)
        return ans

