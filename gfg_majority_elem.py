#https://practice.geeksforgeeks.org/problems/majority-element/0
#find the element which repeats more than n/2 times in the array

for _ in range(int(input())):
    l_lst = int(input())
    lst = list(map(int,input().split()))
    x = lst[0]
    cnt =0
    for i in range(len(lst)):
        if x == lst[i]:
            cnt+=1
        else:
            if cnt == 0:
                x = lst[i]
                cnt = 1
            else:
                cnt-=1
    cnt=0
    for i in range(l_lst):
        if lst[i] == x:
            cnt+=1

    if cnt > l_lst/2:
        print(x)
    else:
        print(-1)