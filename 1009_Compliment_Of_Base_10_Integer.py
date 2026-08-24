class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0 :
            return 1
        mask=1
        while mask<n:
            mask = (mask<<1)|1
        return mask^n
