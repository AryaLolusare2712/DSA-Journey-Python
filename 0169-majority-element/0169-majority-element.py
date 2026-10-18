class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = Counter(nums)

        for num in set(nums):
            if count[num] > len(nums) // 2:
                return num