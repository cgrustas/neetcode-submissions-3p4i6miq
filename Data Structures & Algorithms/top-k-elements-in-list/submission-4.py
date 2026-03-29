class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequency = [[] for i in range(len(nums) + 1)] # why + 1 here? 
        for num in nums: 
            count[num] = count.get(num, 0) + 1
        
        for num, ct in count.items():
            frequency[ct].append(num)
        
        result = []
        for ct in range(len(frequency) - 1, 0, -1):
            for num in frequency[ct]:
                result.append(num)
                if len(result) == k:
                    return result