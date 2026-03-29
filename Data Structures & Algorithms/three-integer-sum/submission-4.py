# brute force solution:
# iterate through every combination of three numbers, 
# and store the combinations with sums equal to 0
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        zeroSums = []
        sortedNums = sorted(nums)   
    
        for first in range(len(sortedNums) - 2): 
            # since the array is sorted, 
            # we cannot get a zero sum if the first number is positive
            if sortedNums[first] > 0:
                break
            
            # skip duplicates for the first number
            if first > 0 and sortedNums[first] == sortedNums[first - 1]:
                continue
                
            mid, last = first + 1, len(sortedNums) - 1

            while mid < last:
                currentSum = sortedNums[first] + sortedNums[mid] + sortedNums[last]
                if currentSum < 0:
                    mid += 1
                elif currentSum > 0:
                    last -= 1
                else:
                    zeroSums.append([sortedNums[first], sortedNums[mid], sortedNums[last]])
                    # skip duplicates for mid and last numbers
                    while mid < last and sortedNums[mid] == sortedNums[mid + 1]:
                        mid += 1
                    while last > mid and sortedNums[last] == sortedNums[last - 1]:
                        last -= 1

                    # after you have encoded the zero sum combination, increemnt the mid and last numbers. If the mid number is solely incremented and the solution is a zero sum, then you'd be storing duplicates. so that's why you should decrement the 'last' pointer 
                    mid += 1
                    last -= 1
        
        return zeroSums


                    
