class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = defaultdict(int)
        left = 0
        maxcount = 0
        best = 0

        for right in range(len(s)):
            count[s[right]] += 1
            maxcount = max(count[s[right]], maxcount)
            windowsize = right - left + 1

            if windowsize - maxcount > k:
                count[s[left]] -= 1
                left += 1
            best = max(best, right - left + 1)

        return best