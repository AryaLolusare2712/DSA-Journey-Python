class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0

        while n > 0:
            count += n & 1
            n = n >> 1
        
        return count