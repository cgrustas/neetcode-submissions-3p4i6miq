class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) <= k:
            return [max(nums)]

        max_heap = []
        res = []

        for i in range(k):
            max_heap.append((-nums[i], i))
        heapq.heapify(max_heap)
        max_num = max_heap[0][0]
        res.append(-max_num)
        
        for r in range(k, len(nums)):
            l = r - k + 1
            heapq.heappush(max_heap, (-nums[r], r))

            while max_heap[0][1] < l:
                heapq.heappop(max_heap)

            max_num = max_heap[0][0]
            res.append(-max_num)

        return res
            