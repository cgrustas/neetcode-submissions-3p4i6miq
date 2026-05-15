class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(curr, opened, closed):
            if closed > opened: 
                return
            

            if opened + closed == n * 2: 
                res.append("".join(curr))
                return

            # decision to add the open parenthesis
            if opened < n: 
                curr.append("(")
                backtrack(curr, opened + 1, closed)
                curr.pop()

            # decision to add the closed parenthesis
            if closed < opened: 
                curr.append(")")
                backtrack(curr, opened, closed + 1)
                curr.pop()
        
        backtrack([], 0, 0)
        return res