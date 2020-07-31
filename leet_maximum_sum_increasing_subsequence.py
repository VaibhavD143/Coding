"""
Intution:
https://www.geeksforgeeks.org/maximum-sum-increasing-subsequence-using-binary-indexed-tree/
"""
def getMax(bit,ind):
    # ind+=1
    # ind-=(ind&-ind)
    res = bit[ind]
    while ind>0:
        res = max(res,bit[ind])
        ind-=(ind&-ind)
    return res

def update(bit,ind,val):
    ind +=1
    while ind<len(bit):
        bit[ind] = max(bit[ind],val)
        ind+=(ind&-ind)

for _ in range(int(input())):
    n = int(input())
    lst = list(map(int,input().split()))
    # lst.sort()
    i = 0
    ha={}
    for n in sorted(lst):
        if n not in ha:
            ha[n]=i
            i+=1
    bit=[0]*(i+1)
    res = lst[0]
    for n in lst:
        tres = n+getMax(bit,ha[n])
        # print(tres,bit)
        res = max(res,tres)
        update(bit,ha[n],tres)
        # print(bit)
    # print(bit)
    # if 100 in ha:
    #     print(getMax(bit,ha[100]))
    print(res)