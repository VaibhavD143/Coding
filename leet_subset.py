lst = [1,2,3]

res = [[]]
for i in range(len(lst)):
    for j in range(len(res)):
        res.append(res[j]+[lst[i]])
print(res)