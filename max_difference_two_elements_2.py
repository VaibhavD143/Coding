#find i,j with max a[j]-a[i] where j-i>=l

lst = [5, 9, 18, 32, 32, 33, 40, 49, 50, 70, 74, 86, 89, 96, 114, 137, 142, 148, 159, 160, 162, 181, 202, 204, 209, 212, 253, 256, 260, 262, 266, 280, 291, 295, 298, 316, 348, 351, 363, 363, 403, 409, 422, 436, 438, 442, 444, 447, 456, 458, 475, 489, 499, 501, 501, 512, 513, 540, 559, 560, 562, 564, 578, 592, 599, 606, 611, 614, 648, 659, 673, 676, 699, 699, 701, 701, 712, 722, 729, 753, 762, 773, 774, 788, 796, 803, 824, 832, 840, 865, 869, 899, 907, 915, 919, 930, 965, 984, 991, 998]
lst = [2,2,3,4,5,6,7]
lst = list(reversed(lst))
l = 5
left_elem = lst[0]
right_elem = lst[l]
diff = right_elem-left_elem
if left_elem > lst[1]:
    left_elem = lst[1]

for j in range(l+1,len(lst)):
    if lst[j]-left_elem > diff:
        diff = lst[j] - left_elem
    if lst[j-l+1] < left_elem:
        left_elem = lst[j]

print(diff,left_elem)