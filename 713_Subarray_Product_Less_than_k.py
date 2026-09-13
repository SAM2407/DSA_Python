class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1:
            return 0

        n = len(nums)
        i = 0
        count = 0
        product = 1

        for j in range(n):
            product *= nums[j]

            while product >= k:
                product //= nums[i]
                i += 1

            count += j - i + 1

        return count
