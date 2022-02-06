class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        tmp = len(nums)
        setA = list(set(nums))
        if len(setA) == tmp:
            return False
        else:
            return True

# better answer -> same but more pythonic
return len(nums) != len(set(nums))