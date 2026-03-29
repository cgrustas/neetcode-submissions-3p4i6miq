class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        outputs = []

        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                product *= nums[j]
            outputs.append(product)
        return outputs
                

        # for each num in nums
            # if num == 0
                # do not divide by num
                # do not multiply all numbers in list

            # multiply all numbers in list

            # divide by num
                