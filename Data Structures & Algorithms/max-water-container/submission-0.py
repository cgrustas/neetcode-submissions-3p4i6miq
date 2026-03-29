class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxVolume = 0 
        for i in range(len(heights) - 1):
            for j in range(i + 1, len(heights)): 
                minHeight = min(heights[i], heights[j])
                currentVolume = minHeight * (j - i)
                maxVolume = max(maxVolume, currentVolume)

        return maxVolume