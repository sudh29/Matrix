class Solution:
    def median(self, matrix, r, c):
    	#code here 
    	temp=[]
    	for i in matrix:
    	    temp.extend(i)
    	temp.sort()
    	n=r*c
    	idx=(n+1)//2
        return temp[idx-1]
