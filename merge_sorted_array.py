from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l1_idx = m - 1
        l2_idx = n - 1
        sorted_idx = m + n - 1
        
        while l1_idx >= 0 or l2_idx >= 0:
            if l1_idx >= 0 and l2_idx >= 0:
                if nums1[l1_idx] > nums2[l2_idx]:
                    nums1[sorted_idx] = nums1[l1_idx]
                    l1_idx -= 1
                else:
                    nums1[sorted_idx] = nums2[l2_idx]
                    l2_idx -= 1
            elif l1_idx >= 0:
                nums1[sorted_idx] = nums1[l1_idx]
                l1_idx -= 1
            else:
                nums1[sorted_idx] = nums2[l2_idx]
                l2_idx -= 1
            sorted_idx -= 1


class SolutionAlternate:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # helper routine to rotate here
        # O(m + n) for setup, O(1) for space
        # O(m + n) for rotate, O(1) for space
        def reverse(nums: List[int], start_idx: int, end_idx: int) -> None:
            while start_idx < end_idx:
                tmp = nums[start_idx]
                nums[start_idx] = nums[end_idx]
                nums[end_idx] = tmp
                start_idx += 1
                end_idx -= 1
        
        
        def rotate(nums: List[int], m: int, n: int) -> None:
            if m + n == 1:
                # nothing to rotate
                return
            reverse(nums, 0, m + n - 1)
            reverse(nums, 0, n - 1)
            reverse(nums, n, m + n - 1)
            
        # special case 1
        if not nums1:
            for i in range(n):
                nums1[i] = nums2[i]
            return
        
        # special case 2
        if not nums2:
            return
        
        l1_ptr = l2_ptr = 0
        sorted_ptr = m
        while l2_ptr < n or l1_ptr < m:
            if l1_ptr < m and l2_ptr < n:
                if nums1[l1_ptr] < nums2[l2_ptr]:
                    nums1[sorted_ptr] = nums1[l1_ptr]
                    l1_ptr += 1
                else:
                    nums1[sorted_ptr] = nums2[l2_ptr]
                    l2_ptr += 1
                sorted_ptr += 1
                sorted_ptr %= m + n
            else:
                while l1_ptr < m:
                    nums1[sorted_ptr] = nums1[l1_ptr]
                    l1_ptr += 1
                    sorted_ptr += 1
                    sorted_ptr %= m + n
                while l2_ptr < n:
                    nums1[sorted_ptr] = nums2[l2_ptr]
                    l2_ptr += 1
                    sorted_ptr += 1
                    sorted_ptr %= m + n
        rotate(nums1, m, n)
                
        