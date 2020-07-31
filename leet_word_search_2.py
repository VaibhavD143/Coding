"""
Intution:
do dfs on every cell from TRIE
"""
class Solution:
    def findWords(self, mat: List[List[str]], words: List[str]) -> List[str]:
        
        def addWord(word,i):
            ha = dic
            for w in word:
                if w in ha:
                    ha = ha[w]
                else:
                    ha[w] ={}
                    ha = ha[w]
            ha['end'] =i
    
        def dfs(x,y,ha):
            if "end" in ha:
                res.add(words[ha["end"]])
            #this is positioned 2nd because when string end on wall, then it needs to go to next iteration
            #ex: words = ['a']
            # mat = [["a"]]
            if 0>x or x>=len(mat) or 0>y or y>=len(mat[0]):
                return
            
            if mat[x][y] in ha:
                tmp = mat[x][y]
                mat[x][y] = '#'
                for nx,ny in (x+1,y),(x,y+1),(x-1,y),(x,y-1):
                    dfs(nx,ny,ha[tmp])
                mat[x][y] = tmp
            return
    
        res = set()
        dic = {}
        for i,word in enumerate(words):
            addWord(word,i)
            
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                dfs(i,j,dic)
        return res