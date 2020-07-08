for tc in range(int(input())):
    n = int(input())
    lst = list(map(int,input().split()))
    sm = 0
    nsm = 0
    max_sm = lst[0]
    min_sm = lst[0]
    for n in lst:
        sm+=n
        nsm+=n
        max_sm = max(sm,max_sm)
        min_sm = min(nsm,min_sm)
        if sm<0:
            sm=0
        if nsm>0:
            nsm=0
    
    if max_sm<0:
        print("Case #{}: {}".format(tc+1,0))
        continue
    
    sq = [i*i for i in range(int(max_sm**0.5)+1)]
    cnt= [0]*len(sq)
    
    sm =0
    offset = min(0,min_sm)*-1
    ha = [0]*(max_sm+1+offset)
    ha[offset] = 1
    for n in lst:
        sm+=n
        for i,s in enumerate(sq):
            diff = sm-s+offset
            cnt[i]+=ha[diff]
            if diff<=0:
                break
        ha[sm+offset]+=1
    # ha = {sm:1}
    # for n in lst:
    #     sm+=n
    #     for i,s in enumerate(sq):
    #         if sm-s in ha:
    #             cnt[i]+=ha[sm-s]
    #         if sm-s<=min_sm:
    #             break
    #     ha[sm]=ha.get(sm,0)+1
    
    print(min_sm,max_sm)
    print(sq)
    print(cnt)
    print(ha)
    print("Case #{}: {}".format(tc+1,sum(cnt)))

# for tc in range(int(input())):
#     r,c = map(int,input().split())
#     mat = []
#     for _ in range(r):
#         mat.append(input())
#     graph = {}
#     indegree = {}
#     for i in range(r-1):
#         for j in range(c):
#             node = mat[i][j]
#             pre = mat[i+1][j]
#             if node not in indegree:
#                 indegree[node]=0
#             if pre not in graph:
#                 graph[pre]= set()
#             if node == pre:
#                 continue
#             else:
#                 if node not in graph[pre]:
#                     indegree[node]+=1
#                     graph[pre].add(node)
#     print(graph)
#     print(indegree)
#     ss = []
#     for i,val in indegree.items():
#         if not val:
#             ss.append(i)
#     res = []
#     while ss:
#         res.append(ss.pop())
#         for v in graph[res[-1]]:
#             indegree[v]-=1
#             if indegree[v] == 0:
#                 ss.append(v)
#     if len(res) == len(graph):
#         print("Case #{}: ".format(tc+1)+''.join(res))
#     else:
#         print("Case #{}: -1".format(tc+1))
# # for tc in range(int(input())):
# #     n,k = map(int,input().split())
# #     lst = list(map(int,input().split()))
# #     tk = k
# #     i=0
# #     cnt=0
# #     for i in range(n):
# #         if lst[i] == tk:
# #             tk-=1
# #             if tk==0:
# #                 cnt+=1
# #                 tk=k
# #         elif lst[i] == k:
# #             tk=k-1
# #             if tk==0:
# #                 cnt+=1
# #                 tk=k
# #         else:
# #             tk=k
# #     print("Case #{}: {}".format(tc+1,cnt))