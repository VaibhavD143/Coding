"""
left to right scan method from solution
"""
lst = "(((()())))(())))))"
lst = "((((((((((()"
curMax = 0
i=0
while i < len(lst):
    if lst[i] == '(':
        balance =0
        length = 0
        j=i
        while j<len(lst):
            if lst[j]=='(':
                balance+=1
            else:
                balance-=1
            if balance<=0:
                if balance == 0:
                    curMax = max(curMax,length+1)
                else:
                    break
            length+=1
            j+=1
        if balance <=0:
            curMax = max(curMax,length)
        i=j
    else:
        i+=1
i=len(lst)-1
while i >=0 :
    if lst[i] == ')':
        balance =0
        length = 0
        j=i
        while j>=0:
            if lst[j]==')':
                balance+=1
            else:
                balance-=1
            if balance<=0:
                if balance == 0:
                    curMax = max(curMax,length+1)
                else:
                    break
            length+=1
            j-=1
        if balance <=0:
            curMax = max(curMax,length)
        i=j
    else:
        i-=1

print(curMax)
