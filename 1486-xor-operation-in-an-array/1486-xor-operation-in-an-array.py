class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        xor = start

        for i in range(1, n):
            xor ^= start + 2 * i
        
        return xor