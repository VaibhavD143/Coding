st = "abcabcbbdefg"
if len(st) == 0:
    print(0)
    exit
l = 0
r = 1
g_len = 1
dic = {}
dic[st[0]]=0
while r < len(st):
    if dic.get(st[r],0):
        g_len = max(g_len,r-l)
        while l<r:
            if st[l] == st[r]:
                l+=1
                break
            # print(dic[st[l]])
            del dic[st[l]]
            l+=1
        # print(dic,l,r)
    else:
        dic[st[r]] = r
    r+=1
g_len = max(g_len,r-l)
print(g_len)