# prices = [7,1,5,6,7,8,3,6,5,4,13,1]
prices = [1,2]
if not prices:
    print(0)
st = prices
# l = 0
r = 1
cur_min = st[0]
max_diff = 0
while r<len(st):
    cur_min = min(cur_min,st[r])
    max_diff = max(max_diff,st[r]-cur_min)
    r+=1
    # print(r)
    
    
print(max_diff)