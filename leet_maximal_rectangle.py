matrix = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
if not matrix or not matrix[0]:
    print(0)
heights = [0]*(len(matrix[0])+1)
maxArea = 0
for row in matrix:
    for i,val in enumerate(row):
        heights[i] = heights[i]+1 if val == '1' else 0
    st = [-1]
    for i,val in enumerate(heights):
        while val < heights[st[-1]]:
            h = heights[st.pop()]
            w = i-1-st[-1]
            maxArea = max(maxArea,h*w)
        st.append(i)
print(maxArea)