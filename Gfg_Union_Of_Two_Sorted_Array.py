class Solution:
    def findUnion(self, a, b):
        # code here 
        ans = []

        n = len(a)
        m = len(b)

        i = 0
        j = 0

        while i < n and j < m:

            if a[i] == b[j]:
                if not ans or ans[-1] != a[i]:
                    ans.append(a[i])
                i += 1
                j += 1

            elif a[i] < b[j]:
                if not ans or ans[-1] != a[i]:
                    ans.append(a[i])
                i += 1

            else:
                if not ans or ans[-1] != b[j]:
                    ans.append(b[j])
                j += 1

        while i < n:
            if not ans or ans[-1] != a[i]:
                ans.append(a[i])
            i += 1

        while j < m:
            if not ans or ans[-1] != b[j]:
                ans.append(b[j])
            j += 1

        return ans

                
