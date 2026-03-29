class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        heights.append(0)

        for i, h in enumerate(heights):
            while stack and h < stack[-1][1]:
                popped_height = stack.pop()[1]

                # if stack was empty, every bar that to the left was >= popped_height, so left = 0
                # else, the first bar that was to the left is less than, so the furthest to the left is stack[-1][0] + 1                
                left = stack[-1][0] + 1 if stack else 0

                # since the current index 'i' is the first bar smaller than the popped height,
                # the index of the furthest bar still within bounds is right - 1
                right = i - 1

                current_area = popped_height * (right - left + 1)
                max_area = max(max_area, current_area)
            
            stack.append((i, h))
        return max_area
