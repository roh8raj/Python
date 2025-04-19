from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Pointer to the last index of the final merged array
        l = m + n - 1

        # Move m and n to point to the last actual elements of nums1 and nums2
        m -= 1
        n -= 1

        # Step 1: Merge from the end of nums1 and nums2
        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[l] = nums1[m]  # Place larger value at the end of nums1
                m -= 1              # Move pointer in nums1
            else:
                nums1[l] = nums2[n]  # Place larger value from nums2
                n -= 1              # Move pointer in nums2
            l -= 1                  # Move the write pointer to the left

        # Step 2: Copy any remaining elements from nums2 (if any)
        while n >= 0:
            nums1[l] = nums2[n]
            n -= 1
            l -= 1

        # No need to copy the remaining nums1 values—they are already in place
