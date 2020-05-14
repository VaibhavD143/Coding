def validate(chk_str):
	for i,j in zip(chk_str,chk_str[1:]):
		if i == j:
			return False
	return True
n=int(input())
string = input()
set_str = set(string)
set_str = list(set_str)
# print(set_str)
max_len = 0
# ans = 'fuck it!'
for i in range(len(set_str)):
	for j in range(i+1,len(set_str)):
		chk_str = [x for x in string if x==set_str[i] or x==set_str[j]]
		if validate(chk_str):
			max_len = max(max_len,len(chk_str))
print(max_len)