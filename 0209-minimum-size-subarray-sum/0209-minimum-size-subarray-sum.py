class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        best = float('inf')
        left = 0
        currsum = 0

        for right in range(len(nums)):
            currsum += nums[right]

            while currsum >= target:
                best = min(best, right - left + 1)
                currsum -= nums[left]
                left += 1

        return best if best != float('inf') else 0