class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        water = 0
        left = 0
        right = len(height) - 1

        while left < right:
            water = max(water, min(height[left], height[right]) * (right - left))

            if height[left] < height[right]:
                left += 1
            
            else:
                right -= 1

        return water