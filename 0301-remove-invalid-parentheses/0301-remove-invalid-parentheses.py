
from collections import deque

class Solution:
    def removeInvalidParentheses(self, s):
        def isValid(string):
            balance = 0

            for ch in string:
                if ch == '(':
                    balance += 1

                elif ch == ')':
                    balance -= 1

                    # Too many closing brackets
                    if balance < 0:
                        return False

            # All opening brackets must also be matched
            return balance == 0

        queue = deque([s])
        visited = {s}

        answer = []
        found = False

        while queue:
            current = queue.popleft()

            # If valid, this is the minimum-removal level
            if isValid(current):
                answer.append(current)
                found = True

            # Don't generate strings with more removals
            # once we found valid answers
            if found:
                continue

            # Remove one parenthesis at each position
            for i in range(len(current)):
                if current[i] not in '()':
                    continue

                next_string = current[:i] + current[i + 1:]

                if next_string not in visited:
                    visited.add(next_string)
                    queue.append(next_string)

        return answer

