class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        n=len(grid)
        maxLocal=[[0]*(n-2) for _ in range(n-2)]
        for i in range(n-2):
            for j in range(n-2):
                current_max=grid[i][j]
                for x in range(i,i+3,1):
                    for y in range(j,j+3,1):
                        if grid[x][y]>current_max:
                            current_max=grid[x][y]
                maxLocal[i][j]=current_max
        return maxLocal
Solution1=Solution()
grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
print(Solution1.largestLocal(grid))