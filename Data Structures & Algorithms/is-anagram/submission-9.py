class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sHashMap = {}
        tHashMap = {}
        for i in range(len(s)):
            sHashMap[s[i]] = sHashMap.get(s[i], 0) + 1
            tHashMap[t[i]] = tHashMap.get(t[i], 0) + 1

        return sHashMap == tHashMap
