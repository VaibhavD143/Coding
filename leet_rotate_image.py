mat = [
  [-1,2,-3],
  [4,5,6],
  [7,8,9]
]
def pr(mat):
    for row in mat:
        print(row)
    print()
mat = zip(*mat[::-1])
print(mat)