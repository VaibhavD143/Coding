"""
find Longest palindromic substring
https://leetcode.com/problems/longest-palindromic-substring/
"""

def fun(string):
    l_str = len(string)
    g_len = 1
    s_ind = 0
    e_ind = 0
    for i in range(l_str):
        left = i-1
        right = i+1
        t_len = 1
        while left >=0 and right<l_str:
            if string[left] != string[right]:
                break
            left-=1
            right+=1
            t_len+=2
        if t_len> g_len:
            g_len = t_len
            s_ind = left+1
            e_ind = right-1
        left = i-1
        right = i
        t_len = 0
        while left >= 0 and right<l_str:
            if string[left] != string[right]:
                break
            left-=1
            right+=1
            t_len+=2
        if t_len>g_len:
            g_len = t_len
            s_ind=left+1
            e_ind=right-1
    print(string,g_len,s_ind,e_ind,string[s_ind:e_ind+1])

# fun("forgeeksskeegfor")
# fun("abcd")
fun("abccbd")