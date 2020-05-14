"""
Given a string find its lexicographic rank with duplicate
Unsolved:
"""

string = "kona"
string = "bacb"
l_str = len(string)
indxs= [0]*256
mul_fact = 1
for i in range(l_str):
    indxs[ord(string[i])]+=1
    mul_fact *= (i+1)

for i in range(1,256):
    if indxs[i]>1:
        mul_fact/=indxs[i]
    indxs[i]+=indxs[i-1]
res=0
for i in range(l_str):
    if indxs[ord(string[i])]>1:
        print(mul_fact)
        mul_fact=(mul_fact*indxs[ord(string[i])])/(indxs[ord(string[i])]-1)
    mul_fact/=(l_str-i)
    res+=(mul_fact*indxs[ord(string[i])-1])
    for j in range(ord(string[i]),256):
        indxs[j]-=1
    print(mul_fact,res)
    print(indxs[ord('a'):ord('z')+1])
print(int(res+1))