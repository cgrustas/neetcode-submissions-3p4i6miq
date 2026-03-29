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
                sequence_lengths.add(current_sequence_length)
                current_sequence_length = 0
            
            current_sequence_length += 1
        
        sequence_lengths.add(current_sequence_length)
        return max(sequence_lengths)

