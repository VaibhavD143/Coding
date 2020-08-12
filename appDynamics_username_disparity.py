s = "ababa"
def getLPS(s):
    length= 0
    i=1
    lps = [0]*len(s)
    while i<len(s):
        if s[i] == s[length]:
            length+=1
            lps[i] = length
            i+=1
        else:
            if length!=0:
                length=lps[length-1]
            else:
                i+=1