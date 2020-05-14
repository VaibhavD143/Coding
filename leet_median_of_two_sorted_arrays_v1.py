
l_l1 = len(lst1)
l_l2 = len(lst2)

if l_l1>l_l2:
    l_l1,l_l2 = l_l2,l_l1
    lst1,lst2 = lst2,lst1
ind = math.ceil((l_l1+l_l2)/2)-1
disc = 0
ind1 = -1
ind2 = 0
while 1:
    loc_ind21 = binary_search(lst1,lst2[ind2])
    print(loc_ind21)
    if loc_ind21+ind2+2 >ind+1:
        break
    ind1 = loc_ind21
    ind2+=1
#till ind2-1 elem is added and till ind1 is added
print(ind1,loc_ind21,ind2)
rem1 = len(lst1)-(ind1+1)
rem2 = len(lst2)-(ind2)
rem = (ind+1)-(ind1+1)-ind2
if rem == 1:
    if rem2 > 0:
        ind2+=1
    else:
        ind1+=1
elif rem > 1:
    if rem1>0: