class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # for every element that is 1, look at the next element
        # if next element is a 1, add 1 to island
        # for every element that is 1, look at the element below it
        # if the element below it is 1, add 1 to island

        # depth first search on the 1s
        # create a set of traversed positions
        # from every node, go to the next 1 (if there is a next one in any direction)
        # if there are 2 1s, choose any one
        # when there is no 1, stop --> this is 1 island

        #recursion base case --> if grid[i][j] == 1 : island += 1
        NUM_ROWS = len(grid)
        NUM_COL = len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        islands = 0

        def dfs(i, j):
            if (i < 0 or j < 0 or i >= NUM_ROWS or j >= NUM_COL or grid[i][j] == "0"):
                return 

            grid[i][j] = '0'
            for di, dj in directions:
                dfs(i + di, j + dj)

        visited = set((0,0))
        # assuming all rows are the same length 
        for i in range(NUM_ROWS):
            for j in range(NUM_COL):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(i,j)
                    islands += 1
                
        return islands




        