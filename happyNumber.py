class Solution:
    def isHappy(self, n: int) -> bool:
        """
        Determines whether a number is a 'happy number'.

        A happy number is defined by the following process:
        - Starting with any positive integer, replace the number by the sum of the squares of its digits.
        - Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle that does not include 1.
        - Numbers for which this process ends in 1 are happy numbers.

        Args:
            n (int): The input number to check.

        Returns:
            bool: True if the number is a happy number, False otherwise.
        """
        
        seen_numbers = set()

        while n != 1 and n not in seen_numbers:
            seen_numbers.add(n)
            n = self._sum_of_squares_of_digits(n)

        return n == 1

    def _sum_of_squares_of_digits(self, num: int) -> int:
        """
        Helper method to calculate the sum of the squares of digits of a number.

        Args:
            num (int): The number whose digits' squares are to be summed.

        Returns:
            int: The sum of the squares of the digits.
        """
        total = 0
        while num > 0:
            digit = num % 10
            total += digit * digit
            num //= 10
        return total
