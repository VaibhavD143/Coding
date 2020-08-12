def solve(A, B):
    left = [-1]*len(A)
    right = left[:]
    ha={}
    sm = 0
    cur = -1
    for i in range(len(A)):
        if A[i] == '1':
            cur = i
            ha[i] = sm
        else:
            sm+=1
        left[i] = cur
    cur = -1
    for i in range(len(A)-1,-1,-1):
        if A[i] == '1':
            cur = i
        right[i] = cur
    res = []
    print(left)
    print(right)
    print(ha)
    for l,r in B:
        l-=1
        r-=1
        left1 = right[l]
        right1 = left[r]
        if left1 == -1 or right1 == -1 or left1 == right1:
            res.append(0)
            continue
        if left1>right1:
            res.append(-1)
            continue
        res.append(ha[right1]-ha[left1])
    return res
        
A="0100010010"
B = [[1,8],[3,7]]
print(solve(A,B))
