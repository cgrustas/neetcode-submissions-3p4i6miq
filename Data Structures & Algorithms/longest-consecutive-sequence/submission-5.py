class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        distinctNums = set(nums)

        longest = 0
        for num in distinctNums:
            if num - 1 not in distinctNums:
                sequenceNum = num
                length = 0
                while sequenceNum in distinctNums:
                    length += 1
                    sequenceNum += 1
                longest = max(length, longest)
        
        return longest
