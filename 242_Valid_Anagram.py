from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        
        freq = Counter(s)
        for char in t:
            freq[char]-=1
        
        for count in freq.values():
            if count!=0:
                return False
        return True
        
