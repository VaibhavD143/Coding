"""
gyaan:
-instead of using list and 2nd element as a flag,
i could have added one key "end" if word end there o/w no "end" key
- i could have used normal dict.
"""
from collections import defaultdict
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ha=defaultdict(str)

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        mem = self.ha
        for i in word[:-1]:
            # print(mem,i)
            if mem[i]:
                mem=mem[i][0]
            else:
                mem[i]=[defaultdict(str),0]
                mem=mem[i][0]
        if mem[word[-1]]:
            mem[word[-1]][1]=1
        else:
            mem[word[-1]]=[defaultdict(str),1]

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        mem=self.ha
        res=0
        for i in word:
            if mem[i]:
                res=mem[i][1]
                mem=mem[i][0]
            else:
                return False
        return res

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        mem=self.ha
        for i in prefix:
            if mem[i]:
                mem=mem[i][0]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert("wr")
# obj.insert("wz")
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# print(obj.ha)