class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backtrack(opened, closed):
            if opened == closed == n: 
                res.append("".join(stack))
                return

            # decision to add the open parenthesis
            if opened < n: 
                stack.append("(")
                backtrack(opened + 1, closed)
                stack.pop()

            # decision to add the closed parenthesis
            if closed < opened: 
                stack.append(")")
                backtrack(opened, closed + 1)
                stack.pop()
        
        backtrack(0, 0)
        return res