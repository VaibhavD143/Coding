from collections import defaultdict,Counter
str1="abaa"
str2="aba"
def count(string):
    ha = defaultdict(int)
    for i in string:
        ha[i]+=1
    return ha
ha1 = Counter(str1)
ha2 = count(str2)
print(ha1)
for i,v in ha1.items():
    if v>ha2[i]:
        print(False)
        exit(1)
print(True)