class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def condition(idx) -> bool:
            return nums[idx] >= target
        
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if condition(mid):
                r = mid
            else:
                l = mid + 1
        
        if l < len(nums) and nums[l] == target:
            return l
        
        return -1