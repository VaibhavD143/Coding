arr = [3,9, -2, -3, 0, 7, -8, -2]
arr = [-2,0,-4]
arr = [-2]
arr = [0]

t_min = arr[0]
t_max = arr[0]
g_max = arr[0]

for i in range(1,len(arr)):
    if arr[i]<0:
        t_min,t_max = t_max,t_min

    t_min = min(arr[i],t_min*arr[i])
    t_max = max(arr[i],t_max*arr[i])

    g_max = max(t_max,g_max)
print(g_max)