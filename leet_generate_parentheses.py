"""
https://leetcode.com/problems/generate-parentheses/
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses
"""

def para(open,close):
    if open>close:
        return False
    if open == 0:
        return [')'*close]
    
    op = para(open-1,close)
    cl = para(open,close-1)
    res1=[]
    res2=[]
    if op:
        res1 = ['('+s for s in op]
    if cl:
        res2 = [')'+s for s in cl]

    return res1+res2

print(para(4,4))