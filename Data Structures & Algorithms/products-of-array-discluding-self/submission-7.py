class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        prefix_product = 1 
        for i in range(len(nums)):
            output[i] = prefix_product
            prefix_product *= nums[i]
        
        postfix_product = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= postfix_product
            postfix_product *= nums[i]

        return output

# time complexity: O(n)
# space complexity: O(1) (assuming that output doesn't count as space)