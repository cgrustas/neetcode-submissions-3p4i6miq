class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # calculate the prefix product for every position in nums
        # store it with the same index in prefixes[]
        prefixes = []
        prefix_product = 1
        for i in range(len(nums)):
            prefix_product *= nums[i]
            prefixes.append(prefix_product)

        # calculate the postfix product for every position in nums,
        # and store it with the same index in postfixes[]
        postfixes = []
        postfix_product = 1
        for i in range(len(nums) - 1, -1, -1):
            postfix_product *= nums[i]
            postfixes.append(postfix_product)
        postfixes = postfixes[::-1]

        # for each index in nums
        # multiply the prefix/postfix products to the left/right of the index
        # store the result in output[]
        output = []
        for i in range(len(nums)):
            # get the prefix to the left of i
            prefix_product = nums[i]

            if i == 0: 
                prefix_product = 1
            else:
                prefix_product = prefixes[i - 1]

            if len(nums) - i == 1:
                postfix_product = 1
            else:
                postfix_product = postfixes[i + 1]
            
            output.append(prefix_product * postfix_product)
        
        return output