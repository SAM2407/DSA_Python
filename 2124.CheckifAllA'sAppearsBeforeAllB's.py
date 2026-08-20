class Solution(object):
    def checkString(self, s):
        n = len(s)
        flag = True
        for i in range(n-1):
            if s[i]==s[i+1] or s[i]=='a' and s[i+1]=='b':
                continue
            else: 
                flag = False
                break
        return flag
        
        
