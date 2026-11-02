class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        arr = [first] * (len(encoded) + 1)

        for i in range(len(encoded)):
            arr[i + 1] = encoded[i] ^ arr[i]
        
        return arr