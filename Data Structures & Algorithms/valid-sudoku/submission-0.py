class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row = {}
        col = {}
        grid = {}

        for i in range(len(board)):

            for j in range(len(board[i])):

                if board[i][j] == '.':
                    continue

                if board[i][j] not in row:
                    row[board[i][j]] = 0

                row[board[i][j]] += 1
        
                if row[board[i][j]] > 1:
                    return False

            row = {}

        for i in range(len(board)):

            for j in range(len(board[i])):

                if board[j][i] == '.':
                    continue

                if board[j][i] not in col:
                    col[board[j][i]] = 0

                col[board[j][i]] += 1
        
                if col[board[j][i]] > 1:
                    return False

            col = {}


        for i in range(len(board)):

            for j in range(len(board[i])):

                if board[i][j] == '.':
                    continue

                grid_num = (i // 3) * 3 + (j // 3)

                if grid_num not in grid:
                    grid[grid_num] = set()

                if board[i][j] in grid[grid_num]:
                    return False

                grid[grid_num].add(board[i][j])
        
        return True
