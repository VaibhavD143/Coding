"""
https://leetcode.com/problems/domino-and-tromino-tiling/

Available tiles:

XX - domino
XX - tromino
X
and find ways to fill 2*N board!
"""
def fun():
    n = int(input())

    # first = 1
    sec = 2
    third = 5
    pre_sum = 2
    if n==1:
        return 1
    elif n==2:
        return sec
    elif n == 3:
        return third 
    else:
        for i in range(4,n+1):
            cnt_i = third+sec+2*(pre_sum)
            pre_sum +=sec
            sec = third
            third = cnt_i
        return third

print(fun())