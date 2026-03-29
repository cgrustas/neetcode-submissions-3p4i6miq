class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0


        num_set = set(nums)
        longest_sequence = 0

        for num in num_set:
            start_of_sequence = num - 1 not in num_set
            if start_of_sequence:
                sequence_length = 0
                while (num + sequence_length) in num_set:
                    sequence_length += 1
                longest_sequence = max(sequence_length, longest_sequence)

        return longest_sequence


