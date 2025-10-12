import heapq
from typing import List
def minStoneSum(self, piles: List[int], k: int) -> int:
        max_heap = [-pile for pile in piles]
        heapq.heapify(max_heap)
        
        for _ in range(k):
            pile = -heapq.heappop(max_heap)
            new_pile = ((pile + 1) // 2)
            heapq.heappush(max_heap, -new_pile)
        
        count = 0
        for pile in max_heap:
            count += pile
        return -count


# Time Complexity 