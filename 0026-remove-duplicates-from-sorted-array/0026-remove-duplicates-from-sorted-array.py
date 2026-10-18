class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        a = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[a] = nums[i]
                a += 1
        
        return a
       