class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Design the condition function. This is the most difficult and most beautiful part. Needs lots of practice.
        def feasible(bananas_per_hour) -> bool:
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / bananas_per_hour)
                    
                if hours > h:
                    return False
            return True
        
        # Correctly initialize the boundary variables left and right. Only one rule: set up the boundary to include all possible elements;
        left, right = 1, max(piles) 
        while left < right:
            mid = (left + right) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1

        # Decide return value. Is it return left or return left - 1? Remember this: after exiting the while loop, left is the minimal k​ satisfying the condition function;
        return left
