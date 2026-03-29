class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # sort numbers
        sorted_nums = sorted(nums)

        # records the length of each consecutive sequence in sorted_nums
        sequence_lengths = set()
        current_sequence_length = 1

        # iterate through each number in sorted_nums
        for i in range(1, len(sorted_nums)):
            # skip over duplicate numbers
            if sorted_nums[i] == sorted_nums[i - 1]:
                continue
                
            # if consecutive sequence is broken 
            if sorted_nums[i] != sorted_nums[i - 1] + 1:
                # add current_sequence_length to sequence_lengths
                sequence_lengths.add(current_sequence_length)
                
                # set current_sequence_length counter to 0
                current_sequence_length = 0

            # increment current_sequence_length
            current_sequence_length += 1

        # add length of last sequence to sequence_length
        sequence_lengths.add(current_sequence_length)

        return max(sequence_lengths)

