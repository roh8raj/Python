class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Determines if ransomNote can be constructed from the letters in magazine.
        Each letter in magazine can only be used once.

        Args:
        ransomNote (str): The note to construct.
        magazine (str): The string containing letters available.

        Returns:
        bool: True if ransomNote can be constructed, False otherwise.
        """

        # Create a frequency dictionary for characters in magazine
        letter_count = {}

        for char in magazine:
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1

        # Check if ransomNote can be formed using letters in the magazine
        for char in ransomNote:
            if char in letter_count and letter_count[char] > 0:
                letter_count[char] -= 1
            else:
                return False

        return True
