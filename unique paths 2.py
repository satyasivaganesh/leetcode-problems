class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        x=1
        #column
        if grid[0][0]==1:
            return 0
        for i in range(n):
            if grid[0][i]==1:
                x=0
            grid[0][i]=x
        # rows
        y=1
        for k in range(1,m):
            if grid[k][0]==1:
                y=0
            grid[k][0]=y
        for r in range(1,m):
            for c in range(1,n):
                if grid[r][c]==1:
                    grid[r][c]=0
                else:
                    grid[r][c]=grid[r-1][c]+grid[r][c-1]
        return grid[m-1][n-1]
                
