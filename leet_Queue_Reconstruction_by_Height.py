class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        if not people :
            return people
        
        # print(lst)
        # # people = [[x,-v] for x,v in people]
        # people.sort(reverse=True)
        # # print(people)
        # res = []
        # # print(lst)
        # # for i in range(len(A)-1,-1,-1):
        #     # for j in range(i,i+lst[i][1]):
        #     #     lst[j],lst[j+1]=lst[j+1],lst[j]
        # for val,i in people:
        #     res.insert(i,[val,i])
        # return res
        people.sort(key = lambda x: (-x[0], x[1]))
        # print(people)
        output = []
        for p in people:
            output.insert(p[1], p)
        return output