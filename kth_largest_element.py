from random import randint
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # hoare partition
        def partition(l: int, r: int, p: int) -> int:
            pivot_value = nums[p]
            nums[p], nums[r] = nums[r], nums[p]

            store_index = l
            for i in range(l, r):
                if nums[i] < pivot_value:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1
            nums[store_index], nums[r] = nums[r], nums[store_index]
            return store_index

        def quickselect(l: int, r: int, k_smallest: int) -> int:
            if l == r:
                return nums[l]

            # randomly choose pivot
            pivot = randint(l, r)

            # partition around it
            pivot_index = partition(l, r, pivot)

            if pivot_index == k_smallest:
                return nums[k_smallest]
            elif pivot_index > k_smallest:
                # recurse in left half of array
                return quickselect(l, pivot_index - 1, k_smallest)
            else:
                return quickselect(pivot_index + 1, r, k_smallest)

        return quickselect(0, len(nums) - 1, len(nums) - k)
