#approach 1:
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count0=0
        count1=0
        count2=0
        for i in range(len(nums)):
            if nums[i]==0:
                count0+=1
            elif nums[i]==1:
                count1+=1
            else:
                count2+=1
        
        for i in range(len(nums)):
            if count0!=0:
                nums[i]=0
                count0-=1
            elif count1!=0:
                nums[i] = 1
                count1-=1
            else:
                nums[i] = 2
                count2-=1
        return nums


#approach-2:- using three pointer approach 
class Solution:
    def sortColors(self, nums):

        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:

            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low] #swaping is done here 
                low += 1
                mid += 1

            elif nums[mid] == 1:
                mid += 1

            else: 
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
