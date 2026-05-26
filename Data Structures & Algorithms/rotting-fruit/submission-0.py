class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # use breadth first search 
        # get the total number of layers in the graph 

        # TIME COMPLEXITY : O(n*m)

        from collections import deque

        ROWS = len(grid)
        COLS = len(grid[0])

        minutes = 0

        # keeping track of fresh fruits is the only way to know when all fruits have rotted
        fresh = 0

        d = [[0,1], [0, -1], [1, 0], [-1, 0]]

        q = deque()
        # not a reachable set, because
        # seen = set()

        # since we're running this, 
        # the algorithm will run even when there are 2 or more rotten fruits
        # because the queue will just add two source nodes and then during search, 
        # will account for all the child nodes in parallel
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1

        while q and fresh > 0:
            # don't just pick 1 node to pop, pop all elements in a layer within a single loop
            for _ in range(len(q)):
                node = q.popleft()
                r, c = node
                for dr, dc in d:
                    nr = r + dr
                    nc = c + dc
                    if (nr < ROWS and nc < COLS and nr >= 0 and nc >= 0 and grid[nr][nc] == 1):
                        q.append((r + dr, c + dc))
                        grid[nr][nc] = 2
                        fresh -= 1

            minutes += 1
        return minutes if fresh == 0 else -1
                    

                    
        