#approach 1 
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        for i in range(n):
            nums[i]= nums[i]*nums[i]
        nums.sort()
        return nums
#approach 2
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        arr = []
        i=0
        j=len(nums)-1
        while i <=j:
            if abs(nums[i])>abs(nums[j]):
                arr.append(nums[i]*nums[i])
                i+=1
            else:
                arr.append(nums[j]*nums[j])
                j-=1
        arr.reverse()
        return arr
            
