#1 approach  1 with three pointers
class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        m=len(nums)
        ans=[0]*m
        i=0
        j=n
        k=0
        while i<n and j<m:
            ans[k]=nums[i]
            k+=1
            ans[k]=nums[j]
            k+=1
            i+=1
            j+=1
        return ans
             

#2 approach two by two pointer or much more cleaner version
class Solution(object):
    def shuffle(self, nums, n):
        ans = []

        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[i + n])

        return ans
