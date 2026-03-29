# brute force solution:
# iterate through every combination of three numbers, 
# and store the combinations with sums equal to 0
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        zeroSums = []
        nums = sorted(nums)   
    
        for first in range(len(nums) - 2): 
            # since the array is sorted, 
            # we cannot get a zero sum if the first number is positive
            if nums[first] > 0:
                break
            
            # skip duplicates for the first number
            if first > 0 and nums[first] == nums[first - 1]:
                continue
                
            mid, last = first + 1, len(nums) - 1

            while mid < last:
                currentSum = nums[first] + nums[mid] + nums[last]
                if currentSum < 0:
                    mid += 1
                elif currentSum > 0:
                    last -= 1
                else:
                    zeroSums.append([nums[first], nums[mid], nums[last]])
                    # skip duplicates for mid and last numbers
                    while mid < last and nums[mid] == nums[mid + 1]:
                        mid += 1
                    while last > mid and nums[last] == nums[last - 1]:
                        last -= 1

                    # after you have encoded the zero sum combination, increemnt the mid and last numbers. If the mid number is solely incremented and the solution is a zero sum, then you'd be storing duplicates. so that's why you should decrement the 'last' pointer 
                    mid += 1
                    last -= 1
        
        return zeroSums


# time complexity: sorting array + iterating through nums with another iteration within each iteration
#                  = O(nlog(n)) + O(n^2)
#                  = O(n^2)
# space complexity: O(1)
