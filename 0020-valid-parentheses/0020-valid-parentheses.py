class Solution:
    def isValid(self, s):
        stack = []

        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for ch in s:

            # Opening bracket
            if ch in '([{':
                stack.append(ch)

            # Closing bracket
            else:
                if not stack or stack[-1] != pairs[ch]:
                    return False

                stack.pop()

        return len(stack) == 0