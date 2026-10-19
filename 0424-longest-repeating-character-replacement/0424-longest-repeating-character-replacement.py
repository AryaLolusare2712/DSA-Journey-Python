class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = defaultdict(int)
        maxcount = 0
        best = 0
        left = 0

        for right in range(len(s)):
            count[s[right]] += 1
            maxcount = max(maxcount, count[s[right]])
            windowsize = right - left + 1

            if windowsize - maxcount > k:
                count[s[left]] -= 1
                left += 1

            best = max(best, right - left + 1)
        
        return best