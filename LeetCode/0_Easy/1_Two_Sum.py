class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

# O(n) solution
class Solution:
    def twoSum(self, nums, target):
        val_dict = {}
        for i in range(len(nums)):
            if target - nums[i] in val_dict:
                return [i, val_dict[target - nums[i]]]
            val_dict[nums[i]] = i