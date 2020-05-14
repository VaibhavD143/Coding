tri = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

for i in range(1,len(tri)):
    tri[i][0] = tri[i-1][0]+tri[i][0]
    tri[i][-1] = tri[i-1][-1]+tri[i][-1]


for i in range(1,len(tri)):
    for j in range(1,i):
        tri[i][j] = tri[i][j] + min(tri[i-1][j-1],tri[i-1][j])
for row in tri:
    print(row)
print(min(tri[-1]))