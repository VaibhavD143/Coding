lst = [4,0,0,1,0]
lst = [0]
curMax = 0
for i in range(len(lst)):
    curMax = max(curMax,i+lst[i])
    print(i,curMax)
    if curMax >= len(lst)-1:
        print(True)
        exit(1)
    if curMax<= i:
        print(False)
        exit(1)