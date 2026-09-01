from typing import List
from collections import deque


class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        rows = len(classroom)
        cols = len(classroom[0])

        start_row = start_col = 0
        litter_index = {}

        # Starting position aur litter positions find karo
        litter_count = 0

        for row in range(rows):
            for col in range(cols):
                if classroom[row][col] == "S":
                    start_row, start_col = row, col

                elif classroom[row][col] == "L":
                    litter_index[(row, col)] = litter_count
                    litter_count += 1

        # Koi litter nahi hai
        if litter_count == 0:
            return 0

        all_collected = (1 << litter_count) - 1

        # row, col, collected_mask, remaining_energy, moves
        queue = deque([
            (start_row, start_col, 0, energy, 0)
        ])

        # Same position aur mask ke liye maximum energy store karenge
        best_energy = {
            (start_row, start_col, 0): energy
        }

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while queue:
            row, col, mask, remaining, moves = queue.popleft()

            # Energy zero hai toh aage move nahi kar sakte
            if remaining == 0:
                continue

            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                # Grid ke bahar
                if not (0 <= new_row < rows and 0 <= new_col < cols):
                    continue

                # Obstacle
                if classroom[new_row][new_col] == "X":
                    continue

                new_energy = remaining - 1
                new_mask = mask
                cell = classroom[new_row][new_col]

                # Litter collect karo
                if cell == "L":
                    index = litter_index[(new_row, new_col)]
                    new_mask |= (1 << index)

                # Reset area par full energy
                if cell == "R":
                    new_energy = energy

                # Saare litter collect ho gaye
                if new_mask == all_collected:
                    return moves + 1

                state = (new_row, new_col, new_mask)

                # Agar isi state par pehle zyada ya equal energy se
                # aa chuke hain, toh current state useful nahi hai
                if new_energy <= best_energy.get(state, -1):
                    continue

                best_energy[state] = new_energy

                queue.append(
                    (
                        new_row,
                        new_col,
                        new_mask,
                        new_energy,
                        moves + 1
                    )
                )

        return -1