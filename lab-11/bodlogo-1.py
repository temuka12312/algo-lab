class Solution:
    def islandPerimeter(self, grid):
        if not grid or len(grid) == 0:
            return 0

        n = len(grid)
        m = len(grid[0])
        vis = [[False] * m for _ in range(n)]
        perimeter = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not vis[i][j]:
                    perimeter += self.dfs(i, j, grid, vis)

        return perimeter

    def dfs(self, row, col, grid, vis):
        n = len(grid)
        m = len(grid[0])
        vis[row][col] = True

        perimeter = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for direction in directions:
            new_row = row + direction[0]
            new_col = col + direction[1]

            if new_row < 0 or new_row >= n or new_col < 0 or new_col >= m or grid[new_row][new_col] == 0:
                perimeter += 1
            elif not vis[new_row][new_col] and grid[new_row][new_col] == 1:
                perimeter += self.dfs(new_row, new_col, grid, vis)

        return perimeter
