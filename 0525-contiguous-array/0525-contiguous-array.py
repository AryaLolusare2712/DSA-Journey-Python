class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {0 : -1}
        curr = 0
        best = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                curr -= 1
            elif nums[i] == 1:
                curr += 1

            if curr in freq:
                best = max(best, i - freq[curr])
            else:
                freq[curr] = i

        return best