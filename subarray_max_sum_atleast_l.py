"""
find max sum of subarray with length atleast L
"""

#lst = [1,1,1,1,1,1]
lst = [-2,-6,3,2]
# lst = [-8,5,-10,5,-6,-2]
# lst = [2,6,-9,8,5,-10,5,6,2]
l_lst = len(lst)
L = 3
i = 0
maxSum = 0
sind=0
eind =0
while i+L-1<l_lst:
    print("in")
    tsum = sum(lst[i:i+L])
    i = i+L
    while i<l_lst and tsum<=0:
        tsum = tsum-lst[i-L]+lst[i]
        i+=1
    
    if tsum>maxSum:
        maxSum = tsum
        sind = i-L+1
        eind = i
    
    
    while i<l_lst:
        tsum += lst[i]
        i+=1
        if tsum < 0:
            break
        if tsum > maxSum:
            maxSum = tsum
            eind = i
        

print(maxSum)
print(sind,eind)
