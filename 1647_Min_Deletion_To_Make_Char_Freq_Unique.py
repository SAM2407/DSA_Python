from collections import Counter
class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
      #Approach 1
        # freq = list(Counter(s).values())
        # ans = 0

        # for i in range(len(freq)):
        #     while freq[i] > 0 and freq[i] in freq[:i]:
        #         freq[i] -= 1
        #         ans += 1

        # return ans
        freq = Counter(s)
        used = set()
        ans = 0

        for f in freq.values():
            while f > 0 and f in used:
                f -= 1
                ans += 1

            used.add(f)

        return ans

        
