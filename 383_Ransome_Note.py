#approach 1 
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        n=len(ransomNote)
        m=len(magazine)
        if n>m:
            return False
        ransomNote = sorted(ransomNote)
        magazine = sorted(magazine)
        i=0
        j=0
        while i<n and j<m:
            if ransomNote[i]==magazine[j]:
                i+=1
                j+=1
            else:
                j+=1
        if i==n:
            return True
        else:
            return False
        # approach 2 
      from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        freq=Counter(magazine)
        for ch in ransomNote:
            if freq[ch]==0:
                return False
            else:
                freq[ch]-=1
        return True
        
