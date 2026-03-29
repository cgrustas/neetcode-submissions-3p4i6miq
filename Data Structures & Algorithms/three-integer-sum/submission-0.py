# brute force solution:
# iterate through every combination of three numbers, 
# and store the combinations with sums equal to 0
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        zeroSums = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    currentSum = nums[i] + nums[j] + nums[k]
                    currentTriplet = sorted([nums[i], nums[j], nums[k]]) # sorted to avoid same combination but diff permutation
                    if currentSum == 0 and currentTriplet not in zeroSums:
                        if i != j and i != k and j != k: 
                            zeroSums.append(currentTriplet)

        return zeroSums
                        