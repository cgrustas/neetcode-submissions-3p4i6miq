class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        # Input: temperatures = [30,38,30,36,35,40,28]
        # Output: [1,4,1,2,1,0,0]

        for i in range(len(temperatures)):
            
            while stack and temperatures[i] > temperatures[stack[-1]]:
                poppedIdx =  stack.pop()
                res[poppedIdx] = i - poppedIdx
            
            stack.append(i)
        return res




        # i = 0, temps[i] = 30
        # stackIndicies = [0]
        
        # i = 1, temps[i] = 38
        # since 38 > 30
            # poppedIdx = stack.pop()
            # res[poppedIdx] = [i - poppedIdx] -> res[0] = 1
        # stack = [1]
        # res = [1, ...]

        # i = 2, temps[i] = 30
        # 30 <= 38, so push index onto stack
        # decStack = [1, 2]
        
        # i = 3, temps[i] = 36
        # 36 > 30
            # poppedIdx = 2
            # res[2] = 3 - 2 = 1

            # decStack = [1]
            # res = [1, _, 1, ...]
        # 36 <= 38, so decStack = [1, 3]

        # i = 4, temps[i] = 35
        # 35 <= 36, so decStack = [1, 3, 4]
        
        # i = 5, temps[i] = 40
        # 40 > 40
            # poppedIdx = 4
            # decStack = [1, 3]
            # res[4] = 5 - 4
        # 40 > 36
            # poppedIdx = 3
            # decStack = [1]
            # res[3] = 5 - 3 = 2
        # 40 > 38
            # poppedIdx = 1
            # decStack = []
            # res[1] = 5 - 1 = 4
        # decStack is empty, so push 40 onto stack
        # decStack = [5]
        # res = [1, 4, 1, 2, 1, 0, 0]

        # i = 6, temps[i] = 28
        # 28 <= 40, so decStack = [5, 6]


