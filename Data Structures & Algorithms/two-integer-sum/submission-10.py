class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i, num in enumerate(nums):
            desiredOperand = target - num
            if desiredOperand in prevMap:
                return [prevMap.get(desiredOperand), i]
            
            prevMap[num] = i