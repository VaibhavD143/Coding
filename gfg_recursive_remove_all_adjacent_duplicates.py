#UNSOLVED
str = 'acaaabbbacdddd'
# str = 'geeksforgeek'
# str = "aaa"
str = 'ebbccbe'
str = 'mssissipie'
str = 'geeksforgeek'
res = []
l=0
r=l+1
rec_del = None
while r<len(str):
    while r<len(str) and str[l] == str[r]:
        r+=1
    
    if r-l>1:
        l=r
        r=l+1
        continue

    if res and str[l] == res[-1]:
        rec_del = res.pop()
        l+=1
        r=l+1
        continue

    if str[l] == rec_del:
        l+=1
        r=l+1
        continue
    res.append(str[l])
    rec_del = None
    l+=1
    r=l+1
print(res,l,r,rec_del)
if l>=len(str):
    print(res)
elif res and str[l] == res[-1]:
    res.pop()
    print(res)
elif str[l] == rec_del:
    print(res)
else:
    print(res+[str[l]])