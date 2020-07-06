# Count Submatrices With All Ones 1504. 
# ttungl@gmail.com

# Given a rows * columns matrix mat of ones and zeros, return how many submatrices have all ones.

# Example 1:

# Input: mat = [[1,0,1],
#               [1,1,0],
#               [1,1,0]]
# Output: 13
# Explanation:
# There are 6 rectangles of side 1x1.
# There are 2 rectangles of side 1x2.
# There are 3 rectangles of side 2x1.
# There is 1 rectangle of side 2x2. 
# There is 1 rectangle of side 3x1.
# Total number of rectangles = 6 + 2 + 3 + 1 + 1 = 13.
# Example 2:

# Input: mat = [[0,1,1,0],
#               [0,1,1,1],
#               [1,1,1,0]]
# Output: 24
# Explanation:
# There are 8 rectangles of side 1x1.
# There are 5 rectangles of side 1x2.
# There are 2 rectangles of side 1x3. 
# There are 4 rectangles of side 2x1.
# There are 2 rectangles of side 2x2. 
# There are 2 rectangles of side 3x1. 
# There is 1 rectangle of side 3x2. 
# Total number of rectangles = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24.
# Example 3:

# Input: mat = [[1,1,1,1,1,1]]
# Output: 21
# Example 4:

# Input: mat = [[1,0,1],[0,1,0],[1,0,1]]
# Output: 5
 

# Constraints:

# 1 <= rows <= 150
# 1 <= columns <= 150
# 0 <= mat[i][j] <= 1

# reference: https://leetcode.com/problems/count-submatrices-with-all-ones/discuss/720227/Pre-computation-VIDEO-solution-O(m*n*n)

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        # sol 1: dp
        # time O(n*m*n) space O(n*m)
        rows, cols = len(mat), len(mat[0])
        A = [[0]*cols for _ in range(rows)]
        # compute the submats
        for i in range(rows-1,-1,-1):
            cnt = 0
            for j in range(cols-1,-1,-1):
                if mat[i][j] == 1:
                    cnt +=1
                else:
                    cnt = 0
                A[i][j] = cnt
        
        # count the submats
        res = 0
        for i in range(rows):
            for j in range(cols):
                tem = float('inf')
                for k in range(i, rows):
                    tem = min(tem, A[k][j]) 
                    res += tem
        return res






