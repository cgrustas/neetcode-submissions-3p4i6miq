class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxVolume = 0 
        for l in range(len(heights) - 1):
            for r in range(l + 1, len(heights)): 
                minHeight = min(heights[l], heights[r])
                currentVolume = minHeight * (r - l)
                maxVolume = max(maxVolume, currentVolume)

        return maxVolume