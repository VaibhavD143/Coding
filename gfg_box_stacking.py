def maxHeight(height, width, length, n):
    #Code here
    lst =[]
    for i in range(n):
        box = sorted([height[i],width[i],length[i]],reverse =True)
        lst.append(box[:])
        lst.append([box[0],box[2],box[1]])
        lst.append([box[1],box[2],box[0]])
    # dp = [[None]*len(lst) for _ in range(len(lst))]
    lst.sort(key=lambda i:i[0]*i[1])
    dp = [i[-1] for i in lst]
    # print(lst)
    res = 0
    for i in range(1,len(lst)):
        for j in range(i):
            if lst[j][0]<lst[i][0] and lst[j][1]<lst[i][1]:
                dp[i] = max(dp[i],lst[i][2]+dp[j])
        res = max(res,dp[i])
    # print(dp)
    # def rec(prev):
    #     if dp[prev]!= None:
    #         return dp[prev]
    #     h = 0
    #     for i in range(len(lst)):
    #         if lst[i][0]<lst[prev][0] and lst[i][1]<lst[prev][1]:
    #             h = max(h,lst[i][2]+rec(i))
    #     dp[prev] = h
    #     return h
    # res = 0
    # for i in range(len(lst)):
    #     res = max(res,rec(i)+lst[i][2])
    return res
