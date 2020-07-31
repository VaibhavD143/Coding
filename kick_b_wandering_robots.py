for tc in range(int(input())):
    
    C,R,y1,x1,y2,x2 = map(int,input().split())
    x1,y1,x2,y2 = x1-1,y1-1,x2-1,y2-1

    dp1 = [1]*C
    if x1 == 0:
        for j in range(y1,len(dp1)):
            dp1[j] = 0
    
    dp2 = dp1[:]
    for i in range(1,R):
        dp2[0] = 0 if y1 ==0 and x1<=i<=x2 else dp1[0]
        for j in range(1,len(dp1)-1):
            if x1<=i<=x2 and y1<=j<=y2:
                dp2[j] = 0
            else:
                dp2[j] = 0.5*(dp2[j-1]+dp1[j])
        if x1<=i<=x2 and y1<=len(dp1)-1<=y2:
            dp2[-1] = 0.5*dp2[-2]+dp1[-1] 
        dp1,dp2 = dp2,dp1
        print(dp1)
    # mn = min(C-1,R-1)
    # fact =1
    # for i in range(1,mn+1):
    #     fact*=i
    # tot =1
    # for i in range((C+R-2),(C+R-2)-mn,-1):
    #     tot*=i
    # tot = tot/fact
    # print(tot,dp1[-1])
    # print(dp1[-1]/tot)
