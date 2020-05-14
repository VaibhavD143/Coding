#find i,j with max a[j]-a[i] where j>i>=j-l

lst = [10,9,3,4,5,8,6,1,4,3,2,5]
l_lst = len(lst)
l=3
min_lst= [None]*l_lst
ds = [0]

for i in range(1,l_lst):
    # print(i,ds)
    while i-ds[0]>l:
        ds.pop(0)
    min_lst[i] = ds[0]
    while ds and lst[ds[-1]]>lst[i]:
        ds.pop()
    ds.append(i)
diff = lst[1]-lst[min_lst[1]]
ind =1
for i in range(2,l_lst):
    if diff< lst[i]-lst[min_lst[i]]:
        diff=lst[i]-lst[min_lst[i]]
        ind = i
print(diff,ind)