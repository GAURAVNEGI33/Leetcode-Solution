class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left = 0
        frequency = {}
        max_length = 0

        for right in range(len(s)):
            current_char = s[right]

            frequency[current_char] = frequency.get(current_char, 0) + 1

            # Current character 2 se zyada baar aa gaya
            while frequency[current_char] > 2:
                left_char = s[left]
                frequency[left_char] -= 1
                left += 1

            window_length = right - left + 1
            max_length = max(max_length, window_length)

        return max_length