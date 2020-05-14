import sys

def palindromeIndex(s):
    len_str = len(s)
    end = len_str//2
    len_str -= 1
    i=0
    flag = 0 
    while i <= end:
    	if(s[i] == s[len_str-i]):
    		i+=1
    	else:
    		flag =1
    		break
    if(flag == 0):
    	# print('in_1')
    	return -1
    t_i = i
    ans_i=len_str-t_i
    while t_i <= end:
    	if(s[t_i] == s[len_str-t_i-1]):
    		t_i+=1
    	else:
    		flag = 2
    		break
    if(flag == 1):
    	# print('in 2')
    	return ans_i
    ans_i = i
    while i <= end:
    	if(s[i+1] == s[len_str-i]):
    		i+=1
    	else:
    		flag = 3
    		break
    if(flag == 2):
    	# print('in_3')
    	return ans_i
    else:
    	# print('in_3')
    	return -1


q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = palindromeIndex(s)
    print(result)
