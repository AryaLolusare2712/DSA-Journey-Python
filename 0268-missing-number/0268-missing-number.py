class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xor = len(nums)

        for i in range(len(nums)):
            xor ^= i
            xor ^= nums[i]
        
        return xor