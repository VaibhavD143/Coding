"""
https://practice.geeksforgeeks.org/problems/longest-even-length-substring/0
"""
from math import ceil

def is_exist(pre_lst,k,l):
    if k&1:
        k+=1
    start = 0
    mid = k//2
    for i in range(k,l+1):
        if pre_lst[mid]-pre_lst[start] == pre_lst[i]-pre_lst[mid]:
            return True
        start+=1
        mid+=1
    return False

for _ in range(int(input())):
    lst = list(input())
    lst = [int(i) for i in lst]
    l_lst = len(lst)
    pre_lst = [0]
    for i in lst:
        pre_lst.append(pre_lst[-1]+i)

    for i in range(l_lst,-1,-1):
        if is_exist(pre_lst,i,l_lst):
            print(i)
            break
    