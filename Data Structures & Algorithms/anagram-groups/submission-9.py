class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_sublists = []
        # key = sorted string, value = list of original strings that match the sorted string
        groups_by_sorted = {}

        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s not in groups_by_sorted:
                groups_by_sorted[sorted_s] = []

            groups_by_sorted[sorted_s].append(s)
        
        return list(groups_by_sorted.values())

# Time complexity: O(m * nlogn)
# Space complexity: O(m * n)