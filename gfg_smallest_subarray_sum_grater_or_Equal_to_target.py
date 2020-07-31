lst = [1, 4, 45, 6, 0, 19]
target = 51
lst = [1, 10, 5, 2, 7]
target = 9
lst = [1, 11, 100, 1, 0, 200, 3, 2, 1, 250]
target = 280
l = 0
res = float('inf')
sm =0 
for r,val in enumerate(lst):
    sm+=val
    if sm>target:
        while sm>target:
            sm-=lst[l]
            l+=1
        res = min(res,r-l+2)
print(res)