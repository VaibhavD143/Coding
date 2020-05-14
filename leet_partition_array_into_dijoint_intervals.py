lst = [5,0,3,8,6]
lst= [0,1,1,1,1,6,12]
lst = [0,0,0,0,0]
minl = [-1]*len(lst)
minl[-1]=lst[-1]
for j in range(len(lst)-2,-1,-1):
    minl[j]=min(lst[j],minl[j+1])
currMax = lst[0]
for i in range(len(lst)-1):
    currMax=max(currMax,lst[i])
    if currMax <=minl[i+1]:
        print(i+1)
        break