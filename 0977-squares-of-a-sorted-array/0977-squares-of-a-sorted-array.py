class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n

        left = 0
        right = n - 1
        write = n - 1

        while left <= right:
            left_square = nums[left] * nums[left]
            right_square = nums[right] * nums[right]

            if left_square > right_square:
                result[write] = left_square
                left += 1
            else:
                result[write] = right_square
                right -= 1

            write -= 1

        return result