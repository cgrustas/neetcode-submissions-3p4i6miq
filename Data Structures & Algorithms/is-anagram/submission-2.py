class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # solve with hashmaps (dictionaries in python)

        # key: letter, value: number of occurrences in string
        s_hashmap = {}
        for letter in s: 
            if letter not in s_hashmap: 
                s_hashmap[letter] = 0
            s_hashmap[letter] += 1
        
        t_hashmap = {}
        for letter in t: 
            if letter not in t_hashmap:
                t_hashmap[letter] = 0
            t_hashmap[letter] += 1
        
        return s_hashmap == t_hashmap
        