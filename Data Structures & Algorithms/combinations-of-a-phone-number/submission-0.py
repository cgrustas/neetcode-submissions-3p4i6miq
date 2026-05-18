class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digit_to_letters = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno",
            "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        def backtrack(i, letter_combo):
            if i == len(digits):
                res.append("".join(letter_combo))
                return
            
            digit = digits[i]
            letters = digit_to_letters[digit]

            for letter in letters:
                letter_combo.append(letter)
                backtrack(i + 1, letter_combo)
                letter_combo.pop()

        
        if not digits:
            return []

        backtrack(0, [])
        return res