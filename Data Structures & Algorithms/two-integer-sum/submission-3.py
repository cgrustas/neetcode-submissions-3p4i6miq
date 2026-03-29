# one pass method
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # key = number, value = index of number in list

        for i in range(len(nums)):
            # check if the difference between the target 
            # and the current value in the list is in the hashmap
            desired_addend = target - nums[i]
            if desired_addend in hashmap: 
                first_addend_index = hashmap[desired_addend]
                second_addend_index = i
                return [first_addend_index, second_addend_index] 
            
            # if not, add the number/index pair to the dictionary
            hashmap[nums[i]] = i

# time complexity: O(n)
# space complexity: O(n)