from collections import deque
def findOrder(words, N, K):
    # code here
    # return the string containing all k characters in correct order
    chars = set("".join(words))
    graph = {c:set() for c in chars}
    indegree = {c:0 for c in chars}
    for w in range(len(words)-1):
        i1 = i2 = 0
        while i1<len(words[w]) and i2<len(words[w+1]) and words[w][i1] == words[w+1][i2]:
            i1+=1
            i2+=1
        if i1<len(words[w]) and i2<len(words[w+1]):
            ch1 = words[w][i1]
            ch2 = words[w+1][i2]
            if ch2 not in graph[ch1]:
                indegree[ch2]+=1
                graph[ch1].add(ch2)

    print(graph)
    print(indegree)
    ss = deque([])
    for k,v in indegree.items():
        if v==0:
            ss.append(k)
    res = []
    while ss:
        u = ss.popleft()
        res.append(u)
        for v in graph[u]:
            indegree[v]-=1
            if indegree[v] == 0:
                ss.append(v)
    # print(res)
    return "".join(res)