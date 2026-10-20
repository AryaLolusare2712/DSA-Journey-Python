class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
            
        for i in range(len(nums)):
            if i == 0 and nums[i] > nums[i + 1]:
                return  i
            
            elif nums[-1] > nums[-2]:
                return len(nums) - 1

            elif nums[i-1] < nums[i] and nums[i] > nums[i + 1]:
                return i
            