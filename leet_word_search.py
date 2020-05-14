"""
https://leetcode.com/problems/word-search/
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""

"""
left: 0, left-bottom: 1,bottom: 2, right-bottom: 3, right: 4, right-top:5, top: 6,left-top:7.
"""
def isThere(word,ind,mat,r,c,dir):
    
    if len(word) == ind:
        print(ind,r,c,"Done")
        return True

    if dir != 0 and c>0 and word[ind] == mat[r][c-1]:
        mat[r][c-1] = -1
        if isThere(word,ind+1,mat,r,c-1,4):
            print(ind,r,c)
            return True
        mat[r][c-1] = word[ind]
        
    
    # if dir != 1 and c>0 and r<len(mat)-1 and word[ind] == mat[r+1][c-1] and isThere(word,ind+1,mat,r+1,c-1,5):
    #     return True
    
    if dir != 2 and r<len(mat)-1 and word[ind] == mat[r+1][c]:
        mat[r+1][c] = -1
        if isThere(word,ind+1,mat,r+1,c,6):
            print(ind,r,c)
            return True
        mat[r+1][c] = word[ind]
    
    # if dir != 3 and c<len(mat[0])-1 and r<len(mat)-1 and word[ind] == mat[r+1][c+1] and isThere(word,ind,mat,r+1,c+1,7):
    #     return True
    
    if dir != 4 and c<len(mat[0])-1 and word[ind] == mat[r][c+1]:
        mat[r][c+1] = -1
        if isThere(word,ind+1,mat,r,c+1,0):
            print(ind,r,c)
            return True
        mat[r][c+1] = word[ind]
    
    # if dir != 5 and c<len(mat[0])-1 and r>0 and word[ind] == mat[r-1][c+1] and isThere(word,ind+1,mat,r-1,c+1,1):
    #     return True
    
    if dir != 6 and r>0 and word[ind] == mat[r-1][c]:
        mat[r-1][c] = -1
        if isThere(word,ind+1,mat,r-1,c,2):
            print(ind,r,c)
            return True
        mat[r-1][c] = word[ind]
    
    # if dir != 7 and c>0 and r>0 and word[ind] == mat[r-1][c-1]:
    #     if isThere(word,ind+1,mat,r-1,c-1,3):
    #         return True

    return False


mat =[["a","a","a","a"],["a","a","a","a"],["a","a","a","a"]]

# mat = [['A']]
word = "aaaaaaaaaaaaa"
# word =""
flag = 0
if len(word) == 0:
    print(False)
else:
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == word[0]:
                print("in")
                mat[i][j]=-1
                if isThere(word,1,mat,i,j,-1):
                    print("True")
                    flag = 1
                    break
                mat[i][j]=word[0]
        if flag:
            break
    if not flag:
        print("False")