# https://practice.geeksforgeeks.org/problems/-minimum-number-of-coins/0

for _ in range(int(input())):
    curr = [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]
    n = int(input())
    coins = [n+1]*(n+1)
    vals = [0]*(n+1)
    coins[0] = 0
    vals[0] = 0
    for i in range(n+1):
        for cur in curr:
            ind = i+cur
            if ind <= n:
                if coins[i]+1<coins[ind]:
                    coins[ind] = coins[i]+1
                    vals[ind] = cur
    i=n
    # print(n)
    while i>0:
        print(vals[i],end=" ")
        i -= vals[i]
    print()
    # print(coins)
    # print(vals)