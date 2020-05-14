import time
h = [4,1,4,10]
w = [6,2,5,12]
l = [7,3,6,32]

h = [1,4,3]
w = [2,5,4]
l = [3,6,1]

h = list(range(1,101))
w = list(range(1,101))
l = list(range(1,101))

# lst = [[min(x,y),max(x,y),z]+[min(y,z),max(y,z),x]+ [min(x,z),max(x,z),y] for lst in zip(h,w,l)]
def max_height(ind):
    global dp,lst
    l_max = 0
    for i in range(len(lst)):
        if lst[ind][0]>lst[i][0] and lst[ind][1]>lst[i][1]:
            if dp[i][ind] == None:
                # print(i,ind)
                dp[i][ind] = max_height(i)
            l_max = max(l_max,dp[i][ind])
    return lst[ind][2]+l_max
s = time.time()
# for j in range(1):
lst = [[min(data[i],data[(i+1)%3]),max(data[i],data[(i+1)%3]),data[(i+2)%3]] for i in range(3) for data in zip(h,w,l)]
dp = [[None]*len(lst) for i in range(len(lst))]
g_max = 0
print(len(lst))
for i in range(len(lst)):
    g_max = max(g_max,max_height(i))    
print(g_max)
# print(dp)
print(time.time()-s)