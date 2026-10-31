class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        return ((1 << n.bit_length()) - 1) ^ n