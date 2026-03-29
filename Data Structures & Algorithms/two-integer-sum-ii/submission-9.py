class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r = len(numbers) - 1
        for l in range(len(numbers) - 1):
            while numbers[l] + numbers[r] >= target: 
                if numbers[l] + numbers[r] == target:
                    return [l + 1, r + 1]
                r -= 1
        
        return [-1, -1]