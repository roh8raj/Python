from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Removes all instances of 'val' from the list 'nums' in-place and returns the new length.
        
        The function maintains a count of valid elements and swaps non-'val' elements 
        forward whenever a 'val' is encountered. The relative order of elements can change.

        Parameters:
        nums (List[int]): The input list of integers.
        val (int): The value to be removed from the list.

        Returns:
        int: The number of elements left after removing all instances of 'val'.
        """
        k = 0  # Counter for non-'val' elements

        for i in range(len(nums)):
            if nums[i] == val:
                # Search for the next non-'val' element to swap with
                j = i + 1
                while j < len(nums):
                    if nums[j] != val:
                        # Increment count of valid element
                        k += 1
                        # Swap the current 'val' with a non-'val' from ahead
                        nums[i], nums[j] = nums[j], nums[i]
                        break  # Break inner loop after successful swap
                    else:
                        j += 1
            else:
                # If current element is not 'val', count it as valid
                k += 1

        return k  # Return the count of valid elements
