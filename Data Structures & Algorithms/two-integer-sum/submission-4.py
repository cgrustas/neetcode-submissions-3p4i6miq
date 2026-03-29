# one pass method
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # key : value, value : index
        prevMap = {}
        
        # iterate through nums
        for i, num in enumerate(nums): 
            difference = target - num
            if difference in prevMap: # searches through all of the keys in the hashmap
                return [prevMap[difference], i]   # diff is always smaller because the hashmap stores the previous
                                            # indices. Therefore, the final list will always be sorted from smallest to largest
            # if target sum is not found, add the key/value pair tor the list
            prevMap[num] = i

