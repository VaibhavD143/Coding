lst = [7,1,5,3,6,4]
max_profit = 0
for i in range(1,len(lst)):
    if lst[i]>lst[i-1]:
        max_profit += lst[i]-lst[i-1]
print(max_profit)