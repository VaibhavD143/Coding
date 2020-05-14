"""
def F(S):
    skip = 0
    for x in reversed(S):
        if x == '#':
            skip += 1
        elif skip:
            skip -= 1
        else:
            yield x

return all(x == y for x, y in itertools.izip_longest(F(str1), F(str2)))
"""


import itertools
str1 = list("qzc#")
str2 = list("#abc#")
l =  0
r =  1
while r<len(str1):
    if str1[r] != "#":
        l=r
        r+=1
    else:
        r+=1
        str1[l]='#'
        while l>0 and str1[l]=="#":
            l-=1
l =  0
r =  1
while r<len(str2):
    if str2[r] != "#":
        l=r
        r+=1
    else:
        r+=1
        str2[l]='#'
        while l>0 and str2[l]=="#":
            l-=1
print(str1)
print(str2)
# print(all(x == y for x, y in zip(str1, str2)))
l1 = l2 = 0
while l1<len(str1) and str1[l1] == '#':
        l1+=1
while l2< len(str2) and str2[l2] == '#':
    l2+=1
while l1<len(str1) and l2<len(str2):
    
    if str1[l1] != str2[l2]:
        print("cond2")
        print(False)
        exit(1)
    l1+=1
    l2+=1
    while l1<len(str1) and str1[l1] == '#':
        l1+=1
    while l2< len(str2) and str2[l2] == '#':
        l2+=1
if l1<len(str1) or l2<len(str2):
    print("cond1")
    print(False)
    exit(1)
print(True)
