lst = [2,1,5,6,2,3]
lst.append(0)
st = [-1]
maxArea = 0
for i,val in enumerate(lst):
    while val < lst[st[-1]]:
        h = lst[st.pop()]
        w = i-1-st[-1]
        maxArea = max(maxArea,h*w)
    st.append(i)
print(maxArea)