class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        sum=0
        i=0
        j=len(numbers)-1
        while i<j:
            sum=numbers[i]+numbers[j]
            if sum == target:
                return [i+1,j+1]
            elif sum<target:
                sum = sum-numbers[i]
                i+=1
            else:
                sum=sum-numbers[j]
                j-=1
        return
        
