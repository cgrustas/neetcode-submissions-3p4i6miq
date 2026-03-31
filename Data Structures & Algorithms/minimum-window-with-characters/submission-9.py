class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = defaultdict(int)
        s_count = defaultdict(int)
        res = ""

        if len(t) > len(s):
            return ""

        for c in t:
            t_count[c] += 1

        l = 0
        matches = 0
        for r in range(len(s)):
            if s[r] in t_count:
                s_count[s[r]] += 1

                if s_count[s[r]] == t_count[s[r]]:
                    matches += 1
            
            while matches >= len(t_count):
                if s[l] in t_count:
                    s_count[s[l]] -= 1

                    if s_count[s[l]] < t_count[s[l]]:
                        matches -= 1
                        if not res or r - l + 1 < len(res):
                            res = s[l:r + 1]
                l += 1 # when to advance l?


        return res