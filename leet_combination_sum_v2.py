
lst = [10,2,2,7,2,4,6,1,5]
k = 8
res = [set() for i in range(k+1)]
t_res = [set() for i in range(k+1)]
lst.sort()
for i in lst:
    for j in range(k+1):
        for x in res[j]:
            if i+j > k:
                break
            # res[i+j].add(x+(i,))
            t_res[i+j].add(x+(i,))
    if i<=k:
        t_res[i].add((i,))
    
    for j in range(k+1):
        if t_res[j]:
            res[j]=res[j].union(t_res[j])
    
def pr(st):
    res =st
    for i in range(len(res)):
        print("tot = ",i,"------------------")
        for j in res[i]:
            print(j)
pr(res)
print(res[-1])