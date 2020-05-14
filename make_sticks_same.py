"""
You are given n number of sticks of different lengths.
Length of each stick is given in an array and we had to find the minimum cost required to make all sticks of same length.
(Given that Every stick has a cost associated with it in an array to increase or decrease one unit of length.)
Used ternary search here!
"""

st = [1,100,101]
cost = [1,1,1]
l_st = len(st)
min_s = st[0]
max_s = st[0]
for i in range(1,l_st):
    if st[i] < min_s:
        min_s = st[i]
    if st[i] > max_s:
        max_s = st[i]

def find_cost(st,cost,k):
    t_cost = 0
    for i in range(l_st):
        t_cost+=(abs(st[i]-k)*cost[i])
    return t_cost


while max_s-min_s > 2:
    mid1 = min_s + (max_s-min_s)//3
    mid2 = max_s - (max_s-min_s)//3

    left_cost= find_cost(st,cost,mid1)
    right_cost= find_cost(st,cost,mid2)
    # print('-----------------------------------')
    # print(left_cost,right_cost)
    if left_cost > right_cost:
        min_s = mid1
    else:
        max_s = mid2
    # print(min_s,max_s)
print(find_cost(st,cost,(min_s+max_s)//2))