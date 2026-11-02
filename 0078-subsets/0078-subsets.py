class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        result = []

        for i in range(1 << n):
            subset = []

            for j in range(n):
                if (i >> j) & 1:
                    subset.append(nums[j])
            
            result.append(subset)
        
        return result