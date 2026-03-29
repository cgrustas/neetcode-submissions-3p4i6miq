class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxVolume = 0 
        # create two pointers 'l' and 'r', where l points to the 
        # beginning of the list, and r points to the end of the list
        l, r = 0, len(heights) - 1

        while l < r: 
            # find minimum height
            minHeight = min(heights[l], heights[r])

            # compute the volume of the container
            currentVolume = minHeight * (r - l)

            # update max volume
            maxVolume = max(currentVolume, maxVolume)

            # shift the minimum height
            if minHeight == heights[l]: 
                l += 1
            else: 
                r -= 1
        return maxVolume