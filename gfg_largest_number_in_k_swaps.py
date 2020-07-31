from collections import deque
def findMin(s,k,ind,res):

    if k==0 or ind == len(s):
        # print(res[0],s)
        if s>res[0]:
            res[0] = s[:]
        return
    maxdig = max(s[ind:])
    
    if maxdig == s[ind]:
        return findMin(s,k,ind+1,res)
    
    for i in range(ind+1,len(s)):
        if s[i] != maxdig:
            continue
        s[i],s[ind] = s[ind],s[i]
        findMin(s,k-1,ind+1,res)
        s[i],s[ind] = s[ind],s[i]
    return
if __name__ == "__main__":
    for _ in range(int(input())):
        k = int(input())
        s = list(input())
        res = [s[:]]
        findMin(s,k,0,res)
        print(''.join(res[0]))

