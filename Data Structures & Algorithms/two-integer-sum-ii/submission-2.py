class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        for l in range(len(numbers) - 1):
            # initialize right pointer to the last element in the list
            r = len(numbers) - 1


            while l < r or numbers[l] != numbers[r]:            
                if numbers[l] + numbers[r] == target:
                    return [l + 1, r + 1]

                r -= 1
        
        return [-1, -1]