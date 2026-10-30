class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        mask = 0xFFFFFFFF
        while b != 0:
            c = ((a & b) << 1) & mask
            a = (a ^ b) & mask
            b = c

        return a if (a <= 0x7FFFFFFF) else ~(a ^ mask)