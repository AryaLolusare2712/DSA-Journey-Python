class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return ((1 << num.bit_length()) - 1) ^ num