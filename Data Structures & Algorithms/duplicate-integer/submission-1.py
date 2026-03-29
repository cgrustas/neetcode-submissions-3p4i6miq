class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        distinct_nums = set()
        for num in nums:
            if num in distinct_nums:
                return True
            else:
                distinct_nums.add(num)
        # if every number is distinct
        return False