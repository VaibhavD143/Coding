coins = [1,2,5]
amnt = 5
res = [0]*(amnt+1)
res[0] = 1
for coin in coins:
    for i in range(amnt+1):
        if res[i] and coin+i<=amnt:
            res[i+coin]+=res[i]
    print(res)
        