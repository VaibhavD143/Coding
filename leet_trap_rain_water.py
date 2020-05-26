def trap(height) -> int:
    if len(height) <3:
        return 0

    
    end = 0
    p = end
    wat = 0
    while p<len(height):
        start = p
        end = start+1
        c_max = end
        p = end
        while end<len(height):
            if height[end]>=height[start]:
                c_max = start
                p=end
                break
            
            if height[end]>height[c_max]:
                c_max = end
                p = end
            end+=1
        while start<p and p<len(height):
            print(start,c_max,p)
            wat += max(height[c_max]-height[start],0)
            start+=1
        print(wat,end)
    print(wat)

trap([0,1,0,2,1,0,1,3,2,0,2,0])
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        left=[A[0]]
        right=[-1]*len(A)
        right[-1]=A[-1]
        for i in A[1:]:
            left.append(max(left[-1],i))
        for j in range(len(A)-2,-1,-1):
            right[j]=max(right[j+1],A[j])
        # print(A)
        # print(left)
        # print(right)
        water=0
        for i in range(len(A)):
            water+=max(0,min(left[i],right[i])-A[i])
        return water