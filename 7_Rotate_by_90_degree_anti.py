
class Solution:
    
    #Function to rotate matrix anticlockwise by 90 degrees.
    def rotateby90(self,a, n): 
        # code here
        # take transpose
        for i in range(n):
            for j in range(i,n):
                a[i][j],a[j][i]=a[j][i],a[i][j]
        
        for i in range((n//2)):
            for j in range(n):
                temp = a[i][j]
                a[i][j] = a[n-i-1][j]
                a[n-i-1][j] = temp
        return a
        # 147
        # 258
        # 369
        
        # 369  741
        # 258  852
        # 147  963
        
