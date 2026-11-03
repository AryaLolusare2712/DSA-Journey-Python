class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        result = []

        for i in range(len(nums)):
            xor ^= nums[i]
        
        lowerbit = xor & -xor

        a = 0
        b = 0

        for num in nums:
            if num & lowerbit:
                a ^= num

            else:
                b ^= num
        
        return [a, b]