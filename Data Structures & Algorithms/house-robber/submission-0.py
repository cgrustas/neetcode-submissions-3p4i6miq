class Solution:
    def rob(self, nums: List[int]) -> int:
        # case 1: rob this house
            # nums[i] + dfs(i + 2)
        # case 2: do not rob this house
            # dfs(i + 1)
        
        memo = [None] * len(nums)
    
        def dfs(i):
            if i >= len(nums): 
                return 0
            
            if not memo[i]: 
                memo[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))
                
            return memo[i]

        return dfs(0)