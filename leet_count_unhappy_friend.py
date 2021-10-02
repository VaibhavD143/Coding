class Solution:
    def unhappyFriends(self, n: int, pref: List[List[int]], pairs: List[List[int]]) -> int:
        mapOrder = [{val:i for i,val in enumerate(row)} for row in pref]
        ans = 0
        # print(mapOrder)
        for i in range(len(pairs)):
            p1 = pairs[i]
            f1,f2 = False,False
            for j in range(len(pairs)):
                if i==j:
                    continue
                p2 = pairs[j]
                if not f1:
                    #p1[0]p2[0]
                    if mapOrder[p1[0]][p1[1]]>mapOrder[p1[0]][p2[0]] and mapOrder[p2[0]][p2[1]]>mapOrder[p2[0]][p1[0]]:
                        ans+=1
                        f1 = True
                    #p1[0]p2[1]
                    elif mapOrder[p1[0]][p1[1]]>mapOrder[p1[0]][p2[1]] and mapOrder[p2[1]][p2[0]]>mapOrder[p2[1]][p1[0]]:
                        ans+=1
                        f1 =True
                if not f2:
                    #p1[1]p2[0]
                    if mapOrder[p1[1]][p1[0]]>mapOrder[p1[1]][p2[0]] and mapOrder[p2[0]][p2[1]]>mapOrder[p2[0]][p1[1]]:
                        ans+=1
                        f2 =True
                    #p1[1]p2[1]
                    elif mapOrder[p1[1]][p1[0]]>mapOrder[p1[1]][p2[1]] and mapOrder[p2[1]][p2[0]]>mapOrder[p2[1]][p1[1]]:
                        ans+=1
                        f2 =True
                    # print(ans)
        return ans