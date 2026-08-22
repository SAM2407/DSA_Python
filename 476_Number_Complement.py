class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num==0:
            return 1
        mask =1
        while mask<num:
            mask = (mask<<1)|1
        
        return mask^num
        
