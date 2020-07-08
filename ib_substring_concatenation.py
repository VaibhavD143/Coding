from collections import Counter
class Solution:
    # @param A : string
    # @param B : tuple of strings
    # @return a list of integers
    def findSubstring(self, A, B):
        if not A or not B:
            return []
        def isValid(s):
            nonlocal wordcount
            sublen = len(B[0])
            
            curr = Counter([s[i:i+sublen] for i in range(0,len(s),sublen)])
            return curr == wordcount
        
        charcount = Counter()   #charcter counter of each word of B
        wordcount = Counter(B)  #word count of each word, case when same word occures more than once
        totlen = len(B[0])*len(B)   #total length of words(condition, each word is of same size)
        
        if totlen>len(A):
            return []   
        for word in B:
            charcount +=Counter(word)
        window=Counter()    #current window char counter
        #counting window for A[0:totlen]
        for i in range(totlen):
            if A[i] in charcount:
                window[A[i]]+=1
        res=[]
        #initial case
        if window == charcount and isValid(A[:totlen]):
            res.append(0)
        
        for i in range(1,len(A)-totlen+1):
            if A[i-1] in charcount:
                window[A[i-1]]-=1
            if A[i+totlen-1] in charcount:
                window[A[i+totlen-1]]+=1
            # print(i,A[i:i+totlen],window,charcount)
            #if window's character counter matches with required char counter
            if window == charcount:
                if isValid(A[i:i+totlen]):
                    res.append(i)
        return res