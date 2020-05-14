prices = [3,3,5,0,0,3,1,4]
prices = [1,2,3,4,5]
prices = [7,6,4,3,1]
prices = [7,1,5,3,6,4]

l_r = [0]*len(prices)
r_l = [0]*len(prices)
c_min = prices[0]
c_max = prices[-1]

for i in range(1,len(prices)-1):
    if c_min>prices[i]:
        c_min = prices[i]
        l_r[i] = l_r[i-1]
    else:
        l_r[i] = max(l_r[i-1],prices[i]-c_min)
# for i in range(len(prices)-2,-1,-1):
#     if c_max < prices[i]:
#         c_max = prices[i]
#         r_l[i]=r_l[i+1]
#     else:
#         r_l[i] = max(r_l[i+1],c_max-prices[i])

# print(prices)
# print(l_r)
# print(r_l)
# res = 0
# for i in range(len(prices)-1):
#     res = max(res,l_r[i]+r_l[i+1])
res = 0
max_diff = 0
for i in range(len(prices)-2,-1,-1):
    if c_max < prices[i]:
        c_max = prices[i]
        # r_l[i]=r_l[i+1]
    elif max_diff < c_max - prices[i]:
        r_l[i] = max(r_l[i+1],c_max-prices[i])
        max_diff = c_max - prices[i]
    res = max(res,l_r[i]+max_diff)
print(max(res,l_r[-1]))