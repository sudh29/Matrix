class Solution:
    def sortedMatrix(self,N,Mat):
        #code here
        temp=[]
        for i in Mat:
            temp.extend(i)
        temp.sort()
        # print(temp)
        idx=0
        for i in range(N):
            for j in range(N):
                Mat[i][j]=temp[idx+j]
            idx+=N
        return Mat
        
