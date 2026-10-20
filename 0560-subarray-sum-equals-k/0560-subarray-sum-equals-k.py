class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        currsum = 0
        prefix = {0 : 1}
        
        for num in nums:
            currsum += num

            if currsum - k in prefix:
                count += prefix[currsum - k]

            prefix[currsum] = prefix.get(currsum, 0) + 1

        return count