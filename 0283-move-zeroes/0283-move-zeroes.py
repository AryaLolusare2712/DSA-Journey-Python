class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        a = 0
        
        while 0 in nums:
            nums.remove(0)
            a += 1
        
        for i in range(a):
            nums.append(0)