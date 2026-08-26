class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        maxi = max(candies)
        ans = [True]*len(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies>=maxi:
                ans[i]=True
            else:
                ans[i]=False
        return ans
        
