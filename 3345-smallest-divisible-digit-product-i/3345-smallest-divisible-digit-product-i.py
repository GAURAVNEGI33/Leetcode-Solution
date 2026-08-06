class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        current_number = n

        while True:
            digit_product = 1

            for digit in str(current_number):
                digit_product *= int(digit)

            if digit_product % t == 0:
                return current_number

            current_number += 1