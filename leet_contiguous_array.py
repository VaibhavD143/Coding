lst = [1,1,1,0,1,0,0,1,1,1,1,0,1]
lst = [0,0,1]
print(lst)
# lst[0] = 1 if lst[0] else -1
# ha = {0:-1,lst[0]:0}
# maxLen = 0
# for i in range(1,len(lst)):
#     lst[i] = lst[i-1] + 1 if lst[i] else lst[i-1]-1
#     if ha.get(lst[i],None) != None:
#         maxLen = max(maxLen,i-ha[lst[i]])
#     else:
#         print(i,lst,ha)
#         ha[lst[i]]=i
# print(lst)
# print(ha)
# print(maxLen)



ha = {0:-1}
bal = 0
maxLen = 0
for i,val in enumerate(lst):
    bal+= 1 if val else -1
    print(bal,ha)
    if bal in ha:
        maxLen = max(maxLen,i-ha[bal])
    else:
        ha[bal]=i
print(maxLen)


