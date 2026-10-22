class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        xor = 0

        for ch in s:
            xor ^= ord(ch)

        for ch in t:
            xor ^= ord(ch)

        return chr(xor)