class Solution(object):
    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        prefix = [0]

        for i in arr:
            prefix.append(prefix[-1] ^ i)

        result = []
        for l, r in queries:
            result.append(prefix[r + 1] ^ prefix[l])

        return result