from typing import List


class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)

        suffixMatch = [0] * (n + 1)

        j = m - 1

        for i in range(n - 1, -1, -1):
            suffixMatch[i] = suffixMatch[i + 1]

            if j >= 0 and word1[i] == word2[j]:
                suffixMatch[i] += 1
                j -= 1

        answer = []
        j = 0
        mismatchUsed = False

        for i in range(n):
            if j == m:
                break

            # Exact match mil gaya.
            if word1[i] == word2[j]:
                answer.append(i)
                j += 1

           
            elif (
                not mismatchUsed
                and suffixMatch[i + 1] >= m - j - 1
            ):
                answer.append(i)
                j += 1
                mismatchUsed = True

        return answer if j == m else []