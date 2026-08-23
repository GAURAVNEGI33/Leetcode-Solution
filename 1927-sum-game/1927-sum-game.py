class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2

        left_sum = 0
        right_sum = 0

        left_q = 0
        right_q = 0

        for i, ch in enumerate(num):

            # First half
            if i < half:
                if ch == '?':
                    left_q += 1
                else:
                    left_sum += int(ch)

            # Second half
            else:
                if ch == '?':
                    right_q += 1
                else:
                    right_sum += int(ch)

        total_q = left_q + right_q

        # Alice gets the final move
        if total_q % 2 == 1:
            return True

        # Bob wins only if this balancing equation is satisfied
        return 2 * (left_sum - right_sum) != 9 * (right_q - left_q)