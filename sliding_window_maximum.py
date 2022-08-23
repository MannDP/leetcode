from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        
        queue = deque()
        def clean_queue(idx: int):
            # remove old items
            while queue[0] 

            # clean out the queue


