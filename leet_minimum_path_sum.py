grid = [
  [1,2,3]]

# sm = [[float('inf')]*(1+len(grid[0])) for _ in range(1+len(grid))]
# sm[1][1] = grid[0][0]
# for j in range(2,1+len(grid[0])):
#     sm[1][j] = grid[0][j-1] + min(sm[1][j],sm[1][j-1])
# for i in range(2,1+len(grid)):
#     for j in range(1,1+len(grid[0])):
#         sm[i][j] = grid[i-1][j-1] + min(sm[i-1][j],sm[i][j-1])
# print(sm[-1][-1])

for i in range(1,len(grid[0])):
    grid[0][i] = grid[0][i-1] + grid[0][i]
for i in range(1,len(grid)):
    grid[i][0] = grid[i-1][0] + grid[i][0]
for i in range(1,len(grid)):
    for j in range(1,len(grid[0])):
        grid[i][j] = grid[i][j] + min(grid[i-1][j],grid[i][j-1])
print(grid)
print(grid[-1][-1])