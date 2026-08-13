from typing import List


class Solution:
    def longestRepeating(
        self,
        s: str,
        queryCharacters: str,
        queryIndices: List[int]
    ) -> List[int]:

        n = len(s)
        chars = list(s)
        size = 4 * n

        left_char = [""] * size
        right_char = [""] * size
        prefix = [0] * size
        suffix = [0] * size
        best = [0] * size
        length = [0] * size

        # Merge left and right child information
        def pull(node):
            left_child = 2 * node
            right_child = 2 * node + 1

            length[node] = (
                length[left_child] + length[right_child]
            )

            left_char[node] = left_char[left_child]
            right_char[node] = right_char[right_child]

            # Initially prefix comes from left child
            prefix[node] = prefix[left_child]

            # If complete left segment has same character
            # and it connects with right segment
            if (
                prefix[left_child] == length[left_child]
                and right_char[left_child] == left_char[right_child]
            ):
                prefix[node] = (
                    length[left_child] + prefix[right_child]
                )

            # Initially suffix comes from right child
            suffix[node] = suffix[right_child]

            # If complete right segment has same character
            # and it connects with left segment
            if (
                suffix[right_child] == length[right_child]
                and right_char[left_child] == left_char[right_child]
            ):
                suffix[node] = (
                    length[right_child] + suffix[left_child]
                )

            best[node] = max(
                best[left_child],
                best[right_child]
            )

            # Repeating substring crosses the middle boundary
            if right_char[left_child] == left_char[right_child]:
                best[node] = max(
                    best[node],
                    suffix[left_child] + prefix[right_child]
                )

        def build(node, start, end):
            if start == end:
                character = chars[start]

                left_char[node] = character
                right_char[node] = character
                prefix[node] = 1
                suffix[node] = 1
                best[node] = 1
                length[node] = 1
                return

            middle = (start + end) // 2

            build(2 * node, start, middle)
            build(2 * node + 1, middle + 1, end)

            pull(node)

        def update(node, start, end, index, character):
            if start == end:
                left_char[node] = character
                right_char[node] = character
                return

            middle = (start + end) // 2

            if index <= middle:
                update(
                    2 * node,
                    start,
                    middle,
                    index,
                    character
                )
            else:
                update(
                    2 * node + 1,
                    middle + 1,
                    end,
                    index,
                    character
                )

            # Update information while returning upwards
            pull(node)

        build(1, 0, n - 1)

        answer = []

        for index, character in zip(
            queryIndices,
            queryCharacters
        ):
            # Update only if character is actually changing
            if chars[index] != character:
                chars[index] = character
                update(
                    1,
                    0,
                    n - 1,
                    index,
                    character
                )

            # Root contains answer for the complete string
            answer.append(best[1])

        return answer