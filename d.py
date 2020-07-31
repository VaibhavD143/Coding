def rec(lst,left,right,k):
    if left == -1:
        return right+k+2
    if right == len(lst):
        return 
for tc in range(int(input())):
    n,q = map(int,input().split())
    lst = list(map(int,input().split()))

    

    print("Case #{}: {}".format(tc+1," ".join(map(str,res))))