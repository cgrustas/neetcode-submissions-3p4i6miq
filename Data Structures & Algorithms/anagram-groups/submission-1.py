class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        for string in strs: 
            sorted_str = sorted(string)
            for sublist in anagrams: 
                if sorted_str == sorted(sublist[0]): 
                    sublist.append(string)
                    break # you need the break for the 'for-else' clause
            else:
                anagrams.append([string])
        return anagrams

# time complexity: O(n^2)
# space complexity: O(n)