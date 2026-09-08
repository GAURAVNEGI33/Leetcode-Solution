class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        frequency = [0] * 26

        for char in magazine:
            index = ord(char) - ord("a")
            frequency[index] += 1

        for char in ransomNote:
            index = ord(char) - ord("a")
            frequency[index] -= 1

            if frequency[index] < 0:
                return False

        return True