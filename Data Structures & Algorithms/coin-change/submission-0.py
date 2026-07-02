class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(current_amount):
            if current_amount == 0:
                return 0
            if current_amount in memo:
                return memo[current_amount]
            
            min_coins = float("inf")
            for coin in coins: 
                if current_amount - coin < 0:
                    continue
                res = 1 + dfs(current_amount -  coin)
                min_coins = min(min_coins, res)
            
            memo[current_amount] = min_coins
            return min_coins
        
        ans = dfs(amount)
        return ans if ans != float("inf") else -1