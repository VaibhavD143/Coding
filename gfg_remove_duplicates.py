for _ in range(int(input())):
    str1 = input()
    ha ={}
    res=''
    for i in str1:
        if ha.get(i,1):
            res+=i
            ha[i]=0
    print(res)