# brute force method
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

        # time complexity: O(n^2)
        # rationale: each element in the list iterate with 
        # every other element in the list to see if their sum 
        # is equivalent to the target

        # space complexity: O)(1)
        # rationale: each you're not creating any new lists
