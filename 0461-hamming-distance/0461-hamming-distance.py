class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        n = x ^ y
        count = 0

        while n > 0:
            count += 1 & n
            n = n >> 1
        
        return count