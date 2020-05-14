num = 99999999999
num = 1
nums = [num]
while True:
    sm=0
    while num>0:
        sm += (num%10)**2
        num = num//10
    print(sm)
    if sm ==1:
        print(True)
        exit(1)
    elif sm in nums:
        print(False)
        exit(1)
    else:
        nums.append(sm)
        num=sm
