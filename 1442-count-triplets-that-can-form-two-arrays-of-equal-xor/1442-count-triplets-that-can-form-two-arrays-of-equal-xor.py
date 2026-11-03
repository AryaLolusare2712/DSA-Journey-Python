class Solution(object):
    def countTriplets(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count = 0
        prefix = [0]

        for i in arr:
            prefix.append(prefix[-1] ^ i)

        for i in range(len(arr)):
            for k in range(i + 1, len(arr)):
                if prefix[k + 1] == prefix[i]:
                    count += k - i

        return count