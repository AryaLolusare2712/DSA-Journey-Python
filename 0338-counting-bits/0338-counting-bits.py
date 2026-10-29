class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = [0]

        for i in range(1, n + 1):
            count = 0
            a = i

            while a > 0:
                count += 1 & a
                a = a >> 1

            result.append(count)

        return result 