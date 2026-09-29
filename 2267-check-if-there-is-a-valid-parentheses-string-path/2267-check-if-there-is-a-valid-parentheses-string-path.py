class Solution:
    def hasValidPath(self, grid):
        m = len(grid)
        n = len(grid[0])

        # Total path length must be even
        if (m + n - 1) % 2 == 1:
            return False

        # dp[i][j] = set of possible balances at (i, j)
        dp = [[set() for _ in range(n)] for _ in range(m)]

        # Starting cell
        if grid[0][0] == ')':
            return False

        dp[0][0].add(1)

        for i in range(m):
            for j in range(n):

                # Starting cell already processed
                if i == 0 and j == 0:
                    continue

                # Get possible balances from top and left
                possible = set()

                if i > 0:
                    possible |= dp[i - 1][j]

                if j > 0:
                    possible |= dp[i][j - 1]

                for balance in possible:

                    # Update balance according to current cell
                    if grid[i][j] == '(':
                        new_balance = balance + 1
                    else:
                        new_balance = balance - 1

                    # Balance can never become negative
                    if new_balance < 0:
                        continue

                    # Remaining cells after this one
                    remaining = (m - 1 - i) + (n - 1 - j)

                    # We need enough ')' to bring balance to 0
                    if new_balance > remaining:
                        continue

                    dp[i][j].add(new_balance)

        # Valid path must end with balance 0
        return 0 in dp[m - 1][n - 1]