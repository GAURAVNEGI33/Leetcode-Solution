class Solution:
    def reverseParentheses(self, s):
        stack = []
        current = ""

        for ch in s:

            # Opening bracket
            if ch == "(":
                stack.append(current)
                current = ""

            # Closing bracket
            elif ch == ")":
                current = current[::-1]

                # Add reversed part to previous string
                current = stack.pop() + current

            # Normal character
            else:
                current += ch

        return current