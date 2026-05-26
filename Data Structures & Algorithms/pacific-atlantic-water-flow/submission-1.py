class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])

        pacific = set()
        atlantic = set()

        result = []

        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        def dfs(r, c, prevHeight, ocean):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or heights[r][c] < prevHeight or (r, c) in ocean):
                return 
            else:
                ocean.add((r,c))
                for dr, dc in directions:
                    dfs(r + dr, c + dc, heights[r][c], ocean)

        for r in range(ROWS):
            dfs(r, 0, 0, pacific)
            dfs(r, COLS - 1, 0, atlantic)
        
        for c in range(COLS):
            dfs(0, c, 0, pacific)
            dfs(ROWS - 1, c, 0, atlantic)

        for item in pacific:
            if item in atlantic:
                result.append(list(item))

        return result

            

