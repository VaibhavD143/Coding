# s = "20[abc1[x]]3[cd3[xyz]]ef"
s = "10[ab20[x]]"
res = ""

def expand(s,st,ed):
    global dic
    res = ""
    i = st+1
    while i<ed:
        if s[i].isdigit():
            l=i
            while s[i].isdigit():
                i+=1
            res+=expand(s,i,dic[i])*int(s[l:i])

            i=dic[i]+1
        else:
            res+=s[i]
            i+=1
        print(res,i)
    return res

dic = {}
st = []
for i in range(len(s)):
    if s[i] == '[':
        st.append(i)
    elif s[i] == ']':
        dic[st.pop()] = i
print(dic)
print(len(expand(s,-1,len(s))))
