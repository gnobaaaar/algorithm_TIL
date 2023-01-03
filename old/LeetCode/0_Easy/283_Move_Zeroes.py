class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = 0
        i = 0
        length = len(nums) - 1
        while (count < length):
            if nums[i] == 0:
                nums.append(0)
                nums.pop(i)
                count = count + 1
            else:
                count = count + 1
                i = i + 1

# better answer

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1