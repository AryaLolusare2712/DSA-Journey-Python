class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0

        for i in range(32):
            bit = 1 & n
            result = (result << 1) | bit
            n = n >> 1
        
        return result