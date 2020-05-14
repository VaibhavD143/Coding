# https://practice.geeksforgeeks.org/problems/kadanes-algorithm/0

for _ in range(int(input())):
    n = int(input())
    lst = list(map(int,input().split()))
    l_sum = g_sum = lst[0]
    for x in lst[1:]:
        if l_sum < 0:
            l_sum =0
        l_sum+=x
        if l_sum > g_sum:
            g_sum = l_sum
    print(g_sum)