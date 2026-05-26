import heapq

class MedianFinder:

    def __init__(self):
        self.smallerHalf = [] # max heap of min half
        self.largerHalf = [] # min heap of max half + middle value if array is odd

    def addNum(self, num: int) -> None:
        heapq.heappush(self.smallerHalf, -num)
        val = heapq.heappop(self.smallerHalf)
        heapq.heappush(self.largerHalf, -val)

        if len(self.largerHalf) > len(self.smallerHalf) + 1:
            val = heapq.heappop(self.largerHalf)
            heapq.heappush(self.smallerHalf, -val)

    def findMedian(self) -> float:
        if len(self.largerHalf) == len(self.smallerHalf) + 1:
            return self.largerHalf[0]
        else:
            return (-self.smallerHalf[0] + self.largerHalf[0]) / 2


        