image = [[0,0,0],[0,1,1]]
sr = 1
sc = 1
newColor = 2
# if not image:
#     return image
r = len(image)
c = len(image[0])
oldCol = image[sr][sc]
ss =[[sr,sc]]
while ss:
    print(ss)
    pix = ss.pop()
    if 0<=pix[0]-1 and image[pix[0]-1][pix[1]] == oldCol:
        image[pix[0]-1][pix[1]] = newColor
        ss.append([pix[0]-1,pix[1]])
    if pix[0]+1 < r and image[pix[0]+1][pix[1]] == oldCol:
        image[pix[0]+1][pix[1]] == newColor
        ss.append([pix[0]+1,pix[1]])
    if 0<=pix[1]-1 and image[pix[0]][pix[1]-1] == oldCol:
        image[pix[0]][pix[1]-1] == newColor
        ss.append([pix[0],pix[1]-1])
    if pix[1]+1<c and image[pix[0]][pix[1]+1] == oldCol:
        image[pix[0]][pix[1]+1] == newColor
        ss.append([pix[0],pix[1]+1])
    
    image[pix[0]][pix[1]]=newColor
print(image)
    