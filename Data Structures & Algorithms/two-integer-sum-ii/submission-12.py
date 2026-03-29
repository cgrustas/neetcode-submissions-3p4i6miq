class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Make two pointers
        # 'l' points to beginning of list, 'r' points to end of list
        l, r = 0, len(numbers) - 1

        while l <= r: 
            currentSum = numbers[l] + numbers[r]
            if currentSum < target:
                l += 1
            elif currentSum > target:
                r -= 1
            else:
                return [l + 1, r + 1] # add 1 b/c the indices are 1-indexed
