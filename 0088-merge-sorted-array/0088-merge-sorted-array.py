class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums = []

        if m > 0:
            for i in range(m):
                nums.append(nums1[i])
        
        if n > 0:
            for i in range(n):
                nums.append(nums2[i])

        nums.sort()

        for i in range(len(nums)):
            nums1[i] = nums[i]