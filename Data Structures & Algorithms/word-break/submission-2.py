class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def helper(i):
            if i in memo:
                return memo[i]

            if i == len(s):
                memo[i] = True
                return True
            
            for word in wordDict:
                if s[i:].startswith(word):
                    if helper(i + len(word)):
                        return True
            
            memo[i] = False
            return False
            
        
        return helper(0)