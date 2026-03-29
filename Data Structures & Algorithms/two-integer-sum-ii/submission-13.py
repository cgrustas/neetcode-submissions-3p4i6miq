class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0
        index2 = len(numbers) - 1

        while index1 < index2:
            diff = target - numbers[index1]

            if diff < numbers[index2]:
                index2 -= 1
            elif diff > numbers[index2]:
                index1 += 1
            else:
                return [index1 + 1, index2 + 1]

            # 3 - 1 == 2


        
            # if 2 < numbers[index2], index2 should move down


            # let's say target is 7
            # 7 - 1 == 6
            # if 6 > 4
            # move index 1 up