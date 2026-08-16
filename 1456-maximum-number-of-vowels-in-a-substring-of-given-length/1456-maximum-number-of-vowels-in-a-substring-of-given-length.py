class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")

        # First window ke vowels count karo
        vowel_count = 0

        for i in range(k):
            if s[i] in vowels:
                vowel_count += 1

        max_count = vowel_count

        # Window ko slide karo
        for right in range(k, len(s)):
            if s[right] in vowels:
                vowel_count += 1

            if s[right - k] in vowels:
                vowel_count -= 1

            max_count = max(max_count, vowel_count)

        return max_count