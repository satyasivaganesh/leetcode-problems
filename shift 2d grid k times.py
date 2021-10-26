class Solution(object):
    def shiftGrid(self, grid, k):
        m=len(grid)
        n=len(grid[0])
        x=grid[m-1][n-1]
        for y in range(k):
            for i in range(m-1,-1,-1):
                for j in range(n-1,-1,-1):
                    if i==0 and j==0:
                        grid[i][j]=x
                    elif i!=0 and j==0:
                        grid[i][j]=grid[i-1][n-1]
                    else:
                        grid[i][j]=grid[i][j-1]
        return grid
