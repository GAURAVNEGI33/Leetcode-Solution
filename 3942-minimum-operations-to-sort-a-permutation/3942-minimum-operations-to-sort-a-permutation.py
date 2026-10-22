class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        if n == 2:
            return 0 if nums[0] == 0 else 1

        k = nums[0]

        # Case A: rotation of increasing
        if all(nums[i] == (k + i) % n for i in range(n)):
            if k == 0:
                return 0
            return min((n - k) % n, k + 2)

        # Case B: rotation of decreasing
        if all(nums[i] == (k - i) % n for i in range(n)):
            kp = (k + 1) % n
            return 1 + min((n - kp) % n, kp)

        return -1