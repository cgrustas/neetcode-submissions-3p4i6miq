class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            # find frequency of each character in s (key in groups_by_character_frequency)
            character_count = [0] * 26
            for char in s:
                character_count[ord(char) - ord('a')] += 1
            
            key = tuple(character_count)            
            anagrams[key].append(s)
        
        return list(anagrams.values())
            
# Time complexity: O()
            