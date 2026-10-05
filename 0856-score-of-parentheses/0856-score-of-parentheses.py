class Solution:
    def scoreOfParentheses(self, s):
        stack = [0]

        for ch in s:
            if ch == '(':
                # New parentheses group
                stack.append(0)

            else:
                # Get current group's score
                x = stack.pop()

                # "()" = 1
                # "(A)" = 2 * A
                score = max(2 * x, 1)

                # Add score to previous level
                stack[-1] += score

        return stack[0]