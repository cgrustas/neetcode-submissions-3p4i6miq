class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        distinctNums = set();
        for num in nums:
            if (num in distinctNums):
                return True
            distinctNums.add(num)
        return False
