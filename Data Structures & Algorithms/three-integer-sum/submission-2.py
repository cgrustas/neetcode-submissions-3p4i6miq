# brute force solution:
# iterate through every combination of three numbers, 
# and store the combinations with sums equal to 0
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        zeroSums = []
        sortedNums = sorted(nums)
        for i in range(len(sortedNums) - 2):
            for j in range(i + 1, len(sortedNums) - 1):
                for k in range(j + 1, len(sortedNums)):
                    currentSum = sortedNums[i] + sortedNums[j] + sortedNums[k]
                    currentTriplet = [sortedNums[i], sortedNums[j], sortedNums[k]] # sorted to avoid same combination but diff permutation
                    if currentSum == 0 and currentTriplet not in zeroSums:
                        if i != j and i != k and j != k: 
                            zeroSums.append(currentTriplet)

        return zeroSums
                        