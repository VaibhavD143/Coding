from collections import defaultdict
class Solution:
    # @param A : list of strings
    # @return a list of strings
    def prefix(self, A):
        trie= Trie()
        for word in A:
            trie.add(word)
        res=[]
        for word in A:
            res.append(trie.uniquPrefix(word))
        return res

class Trie:
    
    def __init__(self):
        self.ha={}
    
    def add(self,word):
        ha = self.ha
        for i in word:
            if ha.get(i,-1)==-1:
                ha[i]={'freq':0}
            ha[i]["freq"]+=1
            ha=ha[i]

        ha["end"]=True
    
    def uniquePrefix2(self,word):
        ha = self.ha
        ans =""
        for i in word:
            ans+=i
            if ha[i]["freq"]==1:
                return ans
            ha=ha[i]
        


    def uniquPrefix(self,word):
        #we are iterating over word and whenever we find splitting, that means there are more than one word in this path
        #so we include till path into answer
        #till here we have longest common path
        #when we reach end we are supposed to add unique character to make prefix unique, so prefix[0]
        ha = self.ha
        prefix=""
        ans=""
        for i in word:
            prefix+=i
            if len(ha[i])>1:
                ans+=prefix
                prefix=""
            ha=ha[i]
        return ans+prefix[0]
trie = Trie()
trie.add("dog")
trie.add("dot")
trie.add("duck")
print(trie.ha)
print(trie.uniquePrefix2("dog"))
print(trie.uniquePrefix2("dot"))
print(trie.uniquePrefix2("duck"))