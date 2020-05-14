"""
https://www.geeksforgeeks.org/minimum-cost-to-modify-a-string/
Given a string str consisting of lower case alphabets only and an integer K. The task is to find the minimum cost to modify the string such that ascii value difference between any two characters of the given string is less than equal to K.
Following operations can be performed on the string:

Increasing a character: For example, when you increase ‘a’ by 1 it becomes ‘b’. Similarly, if you increase ‘z’ by 1 it becomes ‘a’. Increment is done in cyclic manner.
Decreasing a character: For example, when you decrease ‘a’ by 1 it becomes ‘z’. Similarly, if you decrease ‘z’ by 1 it becomes ‘y’. Decrement is done in cyclic manner.
"""

string = "abcdefghi"
# string = "abcd"
k = 2
k+=1

string = list(string)
l_string = len(string)

min_cnt = 100000
ind = (0,0)
for r in range(k-1,26):
    l = r-k+1
    tcnt = 0
    for i in string:
        val = ord(i)-ord('a')
        if val < l:
            tcnt += min(l-val,val+26-r)
        elif val>r:
            tcnt+= min(val-r,l+26-val)
    if tcnt<min_cnt:
        min_cnt = tcnt
        ind = (l,r)

print(min_cnt,ind)