class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        if len(nums) == 1:
            pass
        elif len(nums) == 2:
            k = k % len(nums)
            if k == 1:
                nums[0], nums[1] = nums[1], nums[0]
        elif len(nums) < k:
            k = k % len(nums)
            if k > 0:
                tmp = nums[len(nums):-k - 1:-1]
                for i in range(k):
                    nums.pop()
                nums.reverse()
                nums.extend(tmp)
                nums.reverse()
        else:
            tmp = nums[len(nums):-k - 1:-1]
            for i in range(k):
                nums.pop()
            nums.reverse()
            nums.extend(tmp)
            nums.reverse()


# better answer
class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        nums[:] = nums[n-k:] + nums[:n-k]


# O(1) space complexity