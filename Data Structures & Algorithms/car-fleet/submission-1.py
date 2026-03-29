class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for p, s in zip(position, speed):
            cars.append((p, s))
        
        cars.sort(reverse=True)

        stack = []

        for pos, spd in cars:
            time = (target - pos) / spd

            if not stack or time > stack[-1]:
                stack.append(time)
        
        return len(stack)
