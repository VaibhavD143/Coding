n = int(input())
tmp_n = n
rev_n = 0
while n>0:
    tmp = n%10
    n = n//10
    rev_n *= 10
    rev_n += tmp

