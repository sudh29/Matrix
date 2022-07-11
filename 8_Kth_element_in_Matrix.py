def kthSmallest(mat, n, k): 
    # Your code goes here
    temp=[]
    for i in mat:
        temp.extend(i)
    temp.sort()
    return temp[k-1]
