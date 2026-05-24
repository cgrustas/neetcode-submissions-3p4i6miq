class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)

        max_heap = [-task_count for task_count in task_counts.values()]
        heapq.heapify(max_heap)
        queue = deque() # (task_count, idle_time)
        time = 0

        while max_heap or queue:
            time += 1
            if max_heap: 
                task_count = 1 + heapq.heappop(max_heap)
                if task_count < 0:
                    queue.append((task_count, time + n))

            if queue and queue[0][1] == time:
                heapq.heappush(max_heap, queue.popleft()[0])
        
        return time