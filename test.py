def solve(N,T,LOCS):
    n,t = N,T
    locs = LOCS
    if not locs:
        return 0
    locs.sort()
    locs = [[0,0]]+locs
    tasks = 0
    ress = [[t,0]]+[[0,0] for _ in range(len(locs)-1)]
    # print(locs)
    for i in range(1,len(locs)):
        loc = locs[i]

        for j in range(i):
            res = ress[j]
            if res[0] >= loc[0]-locs[j][0] + loc[1] + loc[0]:
                if ress[i][1]< res[1]+1:
                    ress[i] = [res[0]-(loc[0]-locs[j][0] + loc[1]),res[1]+1]
                elif ress[i][1] == res[1]+1:
                    ress[i][0] = min(ress[i][0],res[0]-(loc[0]-locs[j][0] + loc[1]))
        # print(loc,ress)
        tasks = max(tasks,ress[i][1])
    return tasks
# n,t = map(int,input().split())
# locs = []
# for i in range(n):
#     loc = list(map(int,input().split()))
#     locs.append(loc)
# print(solve(n,t,locs))
def a():
    f = open('input.txt')
    l = list(map(int,(f.read()[1:-1]).split(',')))
    ans = 1
    for n in l:
        if n < 0:
            ans *= -1
        elif n == 0:
            return 0
    return ans
print(a())