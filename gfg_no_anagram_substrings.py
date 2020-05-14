"""
https://www.geeksforgeeks.org/count-total-anagram-substrings/
"""
string = input()
string = list(string)
l_string = len(string)
sub_freq = {}
for i in range(l_string):
    freq = [0]*26
    for j in range(i,l_string):
        freq[ord(string[j])-ord('a')]+=1
        tfreq= tuple(freq)
        try:
            sub_freq[tfreq] +=1
        except:
            sub_freq[tfreq] = 1
print(sub_freq)
ans = 0
for j in sub_freq.values():
    ans += (j*(j-1))//2
print(ans)