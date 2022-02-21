import random
from typing import List


class Solution:

    # O(n) space
    def __init__(self, nums: List[int]):
        self.original = nums
        self.ordering = list(nums)

    # O(1) complexity

    def reset(self) -> List[int]:
        return self.original

    # O(n) complexity

    def shuffle(self) -> List[int]:
        # using this method is cheating
        # random.shuffle(self.ordering)

        for i in range(len(self.original)):
            swap_idx = random.randrange(i, len(self.original))
            self.ordering[i], self.ordering[swap_idx] = self.ordering[swap_idx], self.ordering[i]
        return self.ordering


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
