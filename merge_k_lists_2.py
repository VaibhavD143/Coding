import math
import random

def Rand(start, end, num): 
    res = [] 
    for j in range(num): 
        res.append(random.randint(start, end)) 
    return res 

def chunk_it(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]
chunks = []
l_chunks = 10
for i in range(l_chunks):
    chunks.append(list(map(int,input().split(','))))


while l_chunks != 1:
    temp = []
    while chunks[0] and chunks[1]:
        if chunks[0][0] > chunks[1][0]:
            temp.append(chunks[1].pop(0))
        else:
            temp.append(chunks[0].pop(0))
    temp.extend(chunks[0])
    temp.extend(chunks[1])
    del chunks[1]
    del chunks[0]
    chunks.append(temp)
    l_chunks -= 1
    # break
print(chunks)
print(len(chunks))
