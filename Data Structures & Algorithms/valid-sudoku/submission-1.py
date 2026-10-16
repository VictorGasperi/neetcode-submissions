class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):

            row = {}

            for j in range(9):

                if board[i][j] == ".":
                    continue

                if board[i][j] not in row:
                    row[board[i][j]] = 0

                row[board[i][j]] += 1

                if row[board[i][j]] > 1:
                    return False

        for i in range(9):

            column = {}

            for j in range(9):

                if board[j][i] == ".":
                    continue

                if board[j][i] not in column:
                    column[board[j][i]] = 0

                column[board[j][i]] += 1

                if column[board[j][i]] > 1:
                    return False

        starts = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6),
                    (6, 0), (6, 3), (6, 6)
        ]

        for start in starts:

            grid = {}

            for i in range(start[0], start[0] + 3):

                for j in range(start[1], start[1] + 3):

                    if board[i][j] == ".":
                        continue

                    if board[i][j] not in grid:
                        grid[board[i][j]] = 0

                    grid[board[i][j]] += 1

                    if grid[board[i][j]] > 1:
                        return False


        return True

