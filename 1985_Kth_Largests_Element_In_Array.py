class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        from functools import cmp_to_key

        def comparator(a, b):
            if len(a)!=len(b):
                return len(a)-len(b)
            return -1 if a < b else 1 if a > b else 0

        nums.sort(key=cmp_to_key(comparator))
        return nums[len(nums)-k]
        
