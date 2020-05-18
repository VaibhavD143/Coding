class Trie():
    def __init__(self):
        self.ha={}
        
    def push(self,word):
        memo = self.ha
        for i in word:
            if i in memo:
                memo=memo[i]
            else:
                memo[i]={}
                memo=memo[i]
        memo["end"]=True
    
    def search(self,word):
        memo =self.ha
        for i in word:
            if i in memo:
                memo=memo[i]
            else:
                return False
        if "end" in memo:
            return True
        return False


    def startsWith(self,word):
        memo = self.ha
        for i in word:
            if i in memo:
                memo=memo[i]
            else:
                return False
        return True

    def __str__(self):
        print(self.ha,end="")
        return ""
