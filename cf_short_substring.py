tc = int(input())
while tc:
    s = input()
    res = ''.join(map(str,[s[i] for i in range(0,len(s),2)]))
    print(res+s[-1])
    tc-=1