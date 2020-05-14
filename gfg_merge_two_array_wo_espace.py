# https://practice.geeksforgeeks.org/problems/merge-two-sorted-arrays/0/
import heapq

for _ in range(int(input())):
    n,m = map(int,input().split())
    if n > m:
        n1 = n
        n2 = m
        lst1 = list(map(int,input().split()))
        lst2 = list(map(int,input().split()))
    else:
        n1 = m
        n2 = n
        lst2 = list(map(int,input().split()))
        lst1 = list(map(int,input().split()))
    heapq.heapify(lst2)
    for i in range(n1):
        # print(lst1[i],lst2[0])
        if lst1[i] > lst2[0]:
            temp = lst1[i]
            lst1[i] = heapq.heappop(lst2)
            heapq.heappush(lst2,temp)
    
    print(*lst1,end =" ")
    while lst2:
        print(heapq.heappop(lst2),end=" ")
    print()