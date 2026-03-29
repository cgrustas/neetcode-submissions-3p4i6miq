class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # solve with hashmaps (dictionaries in python)
        if len(s) != len(t):
            return False # skip all the comparisons if they're clearly not anagrams

        # key: letter, value: number of occurrences in string
        countS, countT = {}, {}
        for i in range(len(s)): 
            letterS, letterT = s[i], t[i]
            if letterS not in countS:
                countS[letterS] = 0
            countS[letterS] += 1

            if letterT not in countT:
                countT[letterT] = 0
            countT[letterT] += 1        

        return countS == countT
        
# time complexity: O(n), or O(s + t)
# space complexity: O(n)