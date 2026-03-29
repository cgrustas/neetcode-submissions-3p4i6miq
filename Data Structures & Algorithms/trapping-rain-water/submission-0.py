class Solution:
    def trap(self, height: List[int]) -> int:
        max_area = 0
        l, r = 0, len(height) - 1
        max_left, max_right = height[0], height[len(height) - 1]

        while l < r:
            if height[l] < height[r]:
                if height[l] > max_left:
                    max_left = height[l]
                else:
                    max_area += max_left - height[l]
                l += 1
            else:
                if height[r] > max_right:
                    max_right = height[r]
                else:
                    max_area += max_right - height[r]
                r -= 1
        return max_area