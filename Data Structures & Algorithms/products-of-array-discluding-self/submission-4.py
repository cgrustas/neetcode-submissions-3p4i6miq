class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        # store the prefix product of each num in output
        # (the prefix product stored in the output index 
        # corresponds with the prefix product for that position in nums)
        prefix_product = 1 # default value
        for i in range(len(nums)):
            output.append(prefix_product)
            prefix_product *= nums[i]
        
        # calculate the postfix product of each num in nums
        # multiply postfix prodcut with the existing 
        # prefix product stored in output
        postfix_product = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= postfix_product
            postfix_product *= nums[i]

        return output