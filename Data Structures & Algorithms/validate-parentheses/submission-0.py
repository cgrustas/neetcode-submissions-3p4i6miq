class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = []

        for c in s:
            if c == "(" or c == "{" or c == "[":
                open_brackets.append(c)            
            else: # c == ")" or c == "}" or c == "}":
                if len(open_brackets) == 0:
                    return False

                open_bracket = open_brackets.pop()

                if c == ")" and open_bracket != "(":
                    return False
                elif c == "}" and open_bracket != "{":
                    return False
                elif c == "]" and open_bracket != "[":
                    return False
        
        return len(open_brackets) == 0
        
