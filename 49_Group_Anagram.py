class Solution(object):
    def groupAnagrams(self, strs):
        mp ={}

        n = len(strs)

        for i in range(n):
            temp = list(strs[i])
            temp.sort()
            temp = ''.join(temp)

            if temp not in mp:
                mp[temp]=[]

            mp[temp].append(strs[i])
        
        ans= []
        for i in mp:
            ans.append(mp[i])

        return ans    
        
