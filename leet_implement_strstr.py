class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def countLSP(pat):
            lsp = [0]*len(pat)
            length =0 
            i=1
            while i<len(pat):
                if pat[length] == pat[i]:
                    length+=1
                    lsp[i] = length
                    i+=1
                else:
                    if length == 0:
                        lsp[i] = 0
                        i+=1
                    else:
                        length = lsp[length-1]
            return lsp
        
        if not needle:
            return 0
        if not haystack:
            return -1
        
        lsp = countLSP(needle)
        i=length = 0
        while i<len(haystack):
            if haystack[i] == needle[length]:
                i+=1
                length+=1
                if length == len(needle):
                    return i-length
            else:
                if length == 0:
                    i+=1
                else:
                    length = lsp[length-1]
        return -1