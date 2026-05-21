import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [stone * -1 for stone in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            stone1 = heapq.heappop(max_heap) * -1
            stone2 = heapq.heappop(max_heap) * -1

            if stone1 > stone2: # x < y
                stone1 = stone1 - stone2
                heapq.heappush(max_heap, stone1 * -1)

        return 0 if not max_heap else max_heap[0] * -1