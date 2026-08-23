class Solution(object):
    def sumGame(self, num):
        """
        :type num: str
        :rtype: bool
        """
        leftcount=0
        rightcount=0
        leftsum=0
        rightsum=0
        n=len(num)
        total=0
        for i in range(n):
            if num[i]=='?':
                if i<n/2:
                    leftcount+=1
                else:
                    rightcount+=1
            else:
                if i<n/2:
                    leftsum=leftsum+(num[i]-'0')
                else:
                    rightsum=rightsum+(num[i]-'0')
        

        total= leftcount+rightcount
        if(total%2==1):
            return True
        left=2*leftsum+9*leftcount
        right=2*rightsum+9*rightcount
        if left==right:
            return False
        return True
