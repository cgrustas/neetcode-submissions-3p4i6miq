class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # sort each string
        s = sorted(s)
        t = sorted(t)

        return s == t

# time complexity: O(nlog(n))
# space complexity: O(n)