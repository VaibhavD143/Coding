"""
https://www.codechef.com/problems/ARITHEXP
"""

def find_min(eq,s,e):
    # print(s,e,"Min")
    global dp_min,dp_max
    if dp_min[s][e] != None:
        return dp_min[s][e]
    if eq[s:e+1].isdigit():
        # print(s,e,int(eq[s:e+1]))
        return int(eq[s:e+1])
    l_val = None
    r_val = None
    res = 10000000000000
    for i in range(s,e+1):
        # print(eq[i])
        if eq[i] == '+':
            if dp_min[s][i-1] == None:
                dp_min[s][i-1] = find_min(eq,s,i-1)
            l_val = dp_min[s][i-1]
            if dp_min[i+1][e] == None:
                dp_min[i+1][e] = find_min(eq,i+1,e)
            r_val = dp_min[i+1][e]
            res = min(res,l_val+r_val)
        if eq[i] == '-':
            if dp_min[s][i-1] == None:
                dp_min[s][i-1] = find_min(eq,s,i-1)
            l_val = dp_min[s][i-1]
            if dp_max[i+1][e] == None:
                dp_max[i+1][e] = find_max(eq,i+1,e)
            r_val = dp_max[i+1][e]
            res = min(res,l_val-r_val)
    dp_min[s][e] = res
    return res

def find_max(eq,s,e):
    global dp_min,dp_max
    if dp_max[s][e] != None:
        return dp_max[s][e]
    if eq[s:e+1].isdigit():
        return int(eq[s:e+1])
    l_val = None
    r_val = None
    res = -10000000000000
    for i in range(s,e+1):
        if eq[i] == '+':
            if dp_max[s][i-1] == None:
                dp_max[s][i-1] = find_max(eq,s,i-1)
            l_val = dp_max[s][i-1]
            if dp_max[i+1][e] == None:
                dp_max[i+1][e] = find_max(eq,i+1,e)
            r_val = dp_max[i+1][e]
            # print(s,i,l_val,i+1,e,r_val)
            res = max(res,l_val+r_val)
        if eq[i] == '-':
            if dp_max[s][i-1] == None:
                dp_max[s][i-1] = find_max(eq,s,i-1)
            l_val = dp_max[s][i-1]
            if dp_min[i+1][e] == None:
                dp_min[i+1][e] = find_min(eq,i+1,e)
            r_val = dp_min[i+1][e]
            res = max(res,l_val-r_val)
    dp_max[s][e] = res
    return res

n = int(input())
eq = input()
dp_min = [[None]*n for i in range(n)]
dp_max = [[None]*n for i in range(n)]
print(find_max(eq,0,n-1)-find_min(eq,0,n-1))