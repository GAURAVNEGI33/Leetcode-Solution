class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        subarray_count = {}

        # Size k ki har possible window
        for start in range(len(nums) - k + 1):
            window = nums[start:start + k]

            # Same window mein duplicate ko ek baar count karo
            unique_numbers = set(window)

            for num in unique_numbers:
                subarray_count[num] = subarray_count.get(num, 0) + 1

        answer = -1

        # Exactly one subarray mein aane wala largest number
        for num, count in subarray_count.items():
            if count == 1:
                answer = max(answer, num)

        return answer