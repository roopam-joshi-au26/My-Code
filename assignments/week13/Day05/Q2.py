'''
Q-2 ) Pascal's Triangle II (5 marks)
https://leetcode.com/problems/pascals-triangle-ii/
(Easy)
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's
triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it
as shown:
'''
class Solution:
    def getRow(self, rowIndex: int):
        tri=[[1], [1,1]]
        for i in range(2, rowIndex+1):
            row=[None]*(i+1)
            row[0]=1
            row[i]=1
            for j in range(1,i):
                row[j]=tri[i-1][j]+tri[i-1][j-1]
            tri.append(row)
        return tri[rowIndex]
