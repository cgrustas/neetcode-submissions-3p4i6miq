class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup_list = set(nums)
        if len(dup_list) < len(nums):
            return True
        return False