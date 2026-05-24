class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Returns true if s2's substring from index l to index r
        # could be a part of a valid permutation of s1. Returns false otherwise

        if len(s1) > len(s2):
            return False

        s1_map = defaultdict(int)
        s2_map = defaultdict(int)

        # build s1 map
        for i in range(len(s1)):
            s1_map[s1[i]] += 1
            s2_map[s2[i]] += 1

        if s1_map == s2_map:
            return True
        
        l = 0
        for r in range(len(s1), len(s2)):
            s2_map[s2[r]] += 1

            s2_map[s2[l]] -= 1
            if s2_map[s2[l]] == 0:
                del s2_map[s2[l]]
            
            l += 1

            if s1_map == s2_map:
                return True
        
        return False
