class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = nums[0]
        returnSum = nums[0]

        if len(nums) == 1:
            return nums[0]

        for i in range(1, len(nums)):
            sum = sum + nums[i]

            if sum < nums[i]:
                sum = nums[i]

            if returnSum < sum:
                returnSum = sum

        return returnSum


# answer
for i in range(1, len(nums)):
        if nums[i-1] > 0:
            nums[i] += nums[i-1]
    return max(nums)


# same accumulate
from itertools import accumulate
    return max(accumulate(nums, lambda x, y: x+y if x > 0 else y))