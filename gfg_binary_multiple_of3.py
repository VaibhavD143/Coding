#https://practice.geeksforgeeks.org/problems/is-binary-number-multiple-of-3/0

num = 1
lst = []
lst.append(num)
for i in range(100):
    num=(num*2)%3
    lst.append(num)
# print(lst)
for _ in range(int(input())):
    string = input()
    ind = 0
    num = 0
    for j in range(len(string)-1,-1,-1):
        if string[j] == '1':
            num+=lst[j]
    if not num%3:
        print(1)
    else:
        print(0)