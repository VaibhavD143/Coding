dic = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
n = "234"
res = list(dic[n[0]])
for i in range(1,len(n)):
    res = [res[j]+dic[n[i]][k] for k in range(len(dic[n[i]])) for j in range(len(res))]
print(res)