class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        max_length = 0
        window_counts = defaultdict(int)
        
        while r < len(s):
            window_counts[s[r]] += 1

            most_frequent_char_count = max(window_counts.values())

            
            # if most frequent character +

            if (r - l + 1) - most_frequent_char_count > k:
                window_counts[s[l]] -= 1
                l += 1

            max_length = max(max_length, (r - l + 1))
            
            r += 1

        return max_length