"""
find subarray with max product
"""
lst = [6, 3, 10, 0, 2,100,1]
lst = [-1, -3, -10, 0, 60]
lst = [-2, -3, 0, -2, -40]
l_lst = len(lst)
ns = [[]]   #index of negatives in single segment(segmented with 0)
zs = [-1]   #index to start with(indices of zeros)
for i in range(l_lst):
    if lst[i] < 0:
        ns[-1].append(i)
    elif lst[i] == 0:
        #if zero then start new segment in new list
        zs.append(i)
        ns.append([])
zs.append(l_lst)    #till here need to iterate
maxProd = 0 #global max
sind = eind = 0 #index of start and end of global max
for j in range(len(ns)):    #for each segment
    l_seg = len(ns[j])     
    tprod = 1   #local product of segment
    if l_seg&1:
        #if segment have odd no of negatives
        fprod = mprod = lprod = 1
        for i in range(zs[j]+1,ns[j][0]+1):
            fprod*=lst[i]   #product till first negative from start of segment
        for i in range(ns[j][0]+1,ns[j][-1]):
            mprod*=lst[i]   #product from first negative till last negative
        for i in range(ns[j][-1],zs[j+1]):
            lprod*=lst[i]   #product from last negative to end of segment
        
        #whichever gives larger product
        if fprod < lprod:
            tprod = fprod*mprod
            if tprod>maxProd:
                maxProd = tprod
                sind = zs[j]+1
                eind = ns[j][-1]-1
        else:
            tprod = mprod*lprod
            if tprod>maxProd:
                maxProd = tprod
                sind = ns[j][0]+1
                eind = zs[j+1]-1

    else:
        #as even no of negatives, multiply them all
        for i in range(zs[j]+1,zs[j+1]):
            tprod*=lst[i]
        print(tprod,"in",zs[j]+1,zs[j+1])
        if tprod>maxProd:
            maxProd = tprod
            sind = zs[j]+1
            eind = zs[j+1]-1

print(lst)
print(maxProd,sind,eind)
