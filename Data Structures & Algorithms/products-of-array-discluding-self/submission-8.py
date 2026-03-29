class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProducts = [1] * len(nums)
        suffixProducts = [1] * len(nums)

        # build prefix products
        prefixProducts[0] = nums[0]
        for i in range(1, len(nums)):
            prefixProducts[i] = prefixProducts[i - 1] * nums[i]

        # build suffix products
        suffixProducts[0] = nums[len(nums) - 1]
        for i in range(len(nums) - 1, 0, -1):
            suffixProducts[len(nums) - i] = suffixProducts[len(nums) - i - 1] * nums[i - 1]

        output = [1] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                output[i] = suffixProducts[len(nums) - i - 2]
            elif i == len(nums) - 1:
                output[i] = prefixProducts[i - 1]
            else:
                output[i] = prefixProducts[i - 1] * suffixProducts[len(nums) - i - 2]
        
        return output