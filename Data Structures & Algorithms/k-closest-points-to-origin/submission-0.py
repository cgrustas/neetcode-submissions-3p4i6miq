import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for point in points:
            x1, y1 = 0, 0
            x2, y2 = point[0], point[1]
            
            squared_distance = (x1 - x2)**2 + (y1 - y2)**2
            heapq.heappush(max_heap, (-squared_distance, point))

            if len(max_heap) > k:
                heapq.heappop(max_heap)
            
        return [point for _, point in max_heap]