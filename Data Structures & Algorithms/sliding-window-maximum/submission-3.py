class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []

        # build decreasing monotonic queue
        for i in range(k):
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)

        res.append(nums[q[0]])

        for r in range(k, len(nums)):
            # remove old elements outside of window
            l = r - k + 1
            while q and q[0] < l:
                q.popleft()

            # pop elements within window that are less than the current number
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            # add new index to queue
            q.append(r)

            # add max number in the window
            res.append(nums[q[0]])

        return res