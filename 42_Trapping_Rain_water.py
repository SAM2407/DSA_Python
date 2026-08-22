class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i=0
        j=len(height)-1
        leftmax=0
        rightmax=0
        ans=0
        while i<j:
            if height[i]<height[j]:
                if height[i]>=leftmax:
                    leftmax=height[i]
                else:
                    ans = ans+leftmax-height[i]
                i+=1
            else:
                if height[j]>=rightmax:
                    rightmax=height[j]
                else:
                    ans=ans+rightmax-height[j]
                j-=1
        return ans
        
