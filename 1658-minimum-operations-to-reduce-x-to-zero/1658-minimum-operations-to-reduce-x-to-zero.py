class Solution:
    def minOperations(self, nums, x):
        target = sum(nums) - x

        # Agar target negative hai,
        # possible nahi hai
        if target < 0:
            return -1

        left = 0
        current_sum = 0
        max_length = -1

        for right in range(len(nums)):
            current_sum += nums[right]

            # Sum target se bada ho gaya
            while current_sum > target and left <= right:
                current_sum -= nums[left]
                left += 1

            # Target sum mil gaya
            if current_sum == target:
                max_length = max(max_length, right - left + 1)

        # Total elements - maximum elements we can keep
        if max_length == -1:
            return -1

        return len(nums) - max_length