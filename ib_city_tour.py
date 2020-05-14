def solve( A, B):
    def rec(marked,avail,ha):
        # print(marked,avail,ha)
        if not avail:
            return 1        
        res= 0
        for i in avail:
            if i>=1 and marked[i-1]==0:
                marked[i]=1
                key = ''.join(map(str,sorted(list(avail.union([i-1])))))
                if ha.get(key,-1) == -1:
                    # tavail = avail[:]
                    # tavail.remove(i)
                    tmp= rec(marked,avail.union([i-1]).difference([i]),ha)
                    ha[key] = tmp%1000000007

                res = (res+ha[key])%1000000007
                marked[i]=0
            elif i<len(marked)-1 and marked[i+1]==0:
                marked[i]=1
                key = ''.join(map(str,sorted(list(avail.union([i+1])))))
                if ha.get(key,-1) == -1:
                    # tavail = avail[:]
                    # tavail.remove(i)
                    tmp= rec(marked,avail.union([i+1]).difference([i]),ha)
                    ha[key] = tmp%1000000007

                res = (res+ha[key])%1000000007
                marked[i]=0
            else:
                marked[i]=1
                key = ''.join(map(str,sorted(list(avail))))
                if ha.get(key,-1) == -1:
                    # tavail = avail[:]
                    # tavail.remove(i)
                    ha[key] = rec(marked,avail.difference([i]),ha)%1000000007
                res = (res+ha[key])%1000000007
                marked[i]=0
        return res%1000000007
    if A<2:
        return -10
    marked=[0]*A
    avail=set()
    for i in B:
        marked[i-1]=1
    if marked[0]==1 and marked[1]==0:
        avail.add(1)
    for i in range(1,len(marked)-1):
        if marked[i]:
            if marked[i-1] ==0:
                avail.add(i-1)
            if marked[i+1] == 0:
                avail.add(i+1)
    if marked[-1]==1 and marked[-2] ==0:
        avail.add(len(marked)-2)
    ha={}
    avail=avail
    print(rec(marked,avail,ha))
print(solve(92,[ 77, 14, 7, 45, 30, 91, 36, 87, 33, 12, 27, 51, 24, 31, 66, 19, 43, 69, 37, 63, 56, 22, 90, 26, 80, 38, 76, 29, 75, 71, 44, 2, 74, 79, 28, 3, 39, 52, 5, 88, 60, 16, 50, 17, 9, 78, 68 ]))